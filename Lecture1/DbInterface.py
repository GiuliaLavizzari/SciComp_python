import oracledb
import json
import time
from functools import wraps


# ----------------------- utilities

# json-like numbering
n_sms= 1 # sm36  
n_towers = 1
n_channels = 25

device_map = {
     "adc0"  : 0
    ,"adc1"  : 1
    ,"dtu"   : 2
    ,"catia" : 3
}

## 'Scritte col sudore delle nostre lacrime' - cit. iykyk
def get_device_key(sm_id, tower_id, board_type, ch_id, device_type):
    assert sm_id == 0
    tower_key  = sm_id     * 100 + tower_id
    board_key  = tower_key * 100 + board_type
    ch_key     = board_key * 100 + ch_id
    device_key = ch_key    * 100 + device_type
    return device_key

def chn_to_board_and_ch_id(chn):
    return chn%5, int(chn/5)

# inutility:
def board_and_ch_id_to_chn(board_type, ch_id):
    return board_type*5 + ch_id
 
def unpack_device_key(device_key):
    device_type = device_map[device_name]
    return 

def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[INFO] Starting DbInterface.{func.__name__}")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"[INFO] Function DbInterface.{func.__name__} executed in {execution_time:.4f} seconds")
        return result 
    return wrapper


# ----------------------- db manager class
class DbInterface:
    connection = None
    handler = None

    def __init__(self, un, pw, dsn):
        try:
            oracledb.init_oracle_client()
            self.connection = oracledb.connect(user=un, password=pw, dsn=dsn)
            self.handler = self.connection.cursor()
            print("[INIT] Connection to", dsn, "established")
        except: 
            raise Exception("Unable to establish connection to", dsn)
    
    def __del__(self):
        self.handler.close()
        self.connection.close()
        print("[DEL] Connection closed cleanly")


    def commit(self):
        self.connection.commit()

    def addRegisterSet(self, notes="Default"):
        sql = """
            INSERT INTO register_sets (notes) 
            VALUES (:1) 
            RETURNING register_set_id INTO :2
        """
        register_set_id = self.handler.var(int)
        self.handler.execute(sql, [notes, register_set_id])
        return register_set_id.getvalue()[0]

    

    def addRegister(self, register_type_id, device_key, register): 
        sql = """
            INSERT INTO registers (register_type_id, device_key, register) 
            VALUES (:1, :2, :3)
            RETURNING register_id INTO :4
        """
        register_id = self.handler.var(int)
        self.handler.execute(sql, [register_type_id, device_key, register, register_id])
        return register_id.getvalue()[0]

    def getRegisterTypeId(self, device_type, address):
        sql = """
            SELECT register_type_id
            FROM register_types
            WHERE device_type = :device_type
            AND address = :address
         """
        self.handler.execute(sql, {'device_type': device_type, 'address': address})
        result = self.handler.fetchone()
        return result[0]

    def addToSetMap(self, register_set_id, register_id):
        sql = """
            INSERT INTO register_set_map (register_set_id, register_id)
            VALUES (:register_set_id, :register_id)
        """
        self.handler.execute(sql, {'register_set_id': register_set_id, 'register_id': register_id})

    @timing_decorator
    def uploadRegisterSetFromJson(self, inputjson, notes):
        print ("[uploadRegisterSetFromJson] Creating new register set with id: ", end="")
        register_set_id = self.addRegisterSet(notes)
        print(register_set_id)

        with open(inputjson, "r") as json_file:
            data = json.load(json_file)
        
        ## Cycle on json to retrieve register values:
        ## Levels are: {tower {channel {device [register values]}}}
        ## You can retrieve the register type id (progr int, prim key) from the register_types table
        ## with such info you can insert the new value and get the register_id (progr int, prim key)
        ## add an entry to register_set_map with pair (register_set_id, register_id)
        for tower_id, tower_dict in data.items():
            for ch_number, channel_dict in tower_dict.items():
                ch_id, board_type = chn_to_board_and_ch_id(int(ch_number))
                for device_name, registers in channel_dict.items():
                    device_type = device_map[device_name]
                    device_key = get_device_key(0, int(tower_id), board_type, ch_id, device_type)
                    for address, register in enumerate (registers):
                        register_type_id = self.getRegisterTypeId(device_type, address)
                        register_id = self.addRegister(register_type_id, device_key, register)
                        self.addToSetMap(register_set_id, register_id)
        self.commit()
        return register_set_id

    @timing_decorator
    def getJsonFromRegisterSet(self, register_set_id):
        thisdict = {}

        for tower_id in range(n_towers):
            thisdict[str(tower_id)]={}
            for ch_number in range(n_channels):
                thisdict[str(tower_id)][str(ch_number)] = {}
                ch_id, board_type = chn_to_board_and_ch_id(int(ch_number))
                for device_name,device_type in device_map.items():
                    device_key = get_device_key(0, tower_id, board_type, ch_id, device_type) 

                    sql = """
                        SELECT registers.register
                        FROM register_set_map
                        JOIN registers ON register_set_map.register_id = registers.register_id
                        JOIN register_types ON registers.register_type_id = register_types.register_type_id
                        WHERE register_set_map.register_set_id = :register_set_id
                          AND registers.device_key = :device_key
                        ORDER BY register_types.address
                    """
                    self.handler.execute(sql, {'register_set_id': register_set_id, 'device_key':device_key })
                    result = self.handler.fetchall()
                    result = list(zip(*result))[0]
                    thisdict[str(tower_id)][str(ch_number)][device_name] = list(result)
        return thisdict 




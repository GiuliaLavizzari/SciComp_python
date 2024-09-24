import oracledb
import json
oracledb.init_oracle_client()

un = 'ecal_p2ug_conf'
dns = 'int2r-s.cern.ch:10121/int2r_lb.cern.ch'
import getpass
pw =  getpass.getpass('\nInsert DB password: ')


def addRegisterSet(connection, handler, notes="Default", commit=False):
    ## commit = False -> to commit with other statemets
    sql = """
        INSERT INTO register_sets (notes) 
        VALUES (:1) 
        RETURNING register_set_id INTO :2
    """
    register_set_id = handler.var(int)
    handler.execute(sql, [notes, register_set_id])
    if commit: connection.commit()
    return register_set_id.getvalue()
    

def addRegister(connection, handler, register_type_id, device_key, register, commit=False) 
    sql = """
        INSERT INTO registers (register_type_id, device_key, register) 
        VALUES (:1, :2, :3)
    """

def main():
    connection = oracledb.connect(user=un, password=pw, dsn=dns)
    handler = connection.cursor()
    set_id = addRegisterSet(connection, handler, notes="DEBUG_DROPME") 
    set_id = addRegisterSet(connection, handler, notes="DEBUG_DROPME")
    print(set_id)
    connection.commit()

if __name__ == "__main__":
    main()

'''
with oracledb.connect(user=un, password=pw, dsn=dns) as connection:
    with connection.cursor() as handler:
        #sql = """select * from register_sets"""
        ## "INSERT INTO register_sets (notes) VALUES (:1) RETURNING register_set_id"
        sql = """
            INSERT INTO register_sets (notes) 
            VALUES (:1) 
            RETURNING register_set_id INTO :2
        """

        print(sql)
        ## Test register_set entry creation
        notes = "DEBUG_DROPME"
        register_set_id = handler.var(int)

        print("Before:", register_set_id.getvalue())
        print("Type:", type(register_set_id.getvalue()))
        handler.execute(sql, [notes, register_set_id])
        connection.commit()
        print("After:", register_set_id.getvalue())
        print("Type:", type(register_set_id.getvalue()))
'''

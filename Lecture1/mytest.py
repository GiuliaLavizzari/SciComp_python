import json
from DbInterface import DbInterface
import getpass

un = 'ecal_p2ug_conf'
dsn = 'int2r-s.cern.ch:10121/int2r_lb.cern.ch'
pw =  getpass.getpass('\nInsert DB password: ')

def main():
    dbi = DbInterface(un, pw, dsn)
    
    register_set_id = dbi.uploadRegisterSetFromJsonMany("all_registers.json", "test from class")
    thisdict = dbi.getJsonFromRegisterSet(register_set_id)
    json.dump(thisdict, open("thisdict.json","w"), indent=4, sort_keys=True)

if __name__ == "__main__":
    main()



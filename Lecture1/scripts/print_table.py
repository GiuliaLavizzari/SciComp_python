import sys
import oracledb
oracledb.init_oracle_client()

un = 'ecal_p2ug_conf'
dns = 'int2r-s.cern.ch:10121/int2r_lb.cern.ch'
import getpass
pw =  getpass.getpass('\nInsert DB password: ')


#comment
with oracledb.connect(user=un, password=pw, dsn=dns) as connection:
    with connection.cursor() as handler:
        if len(sys.argv) < 2:
            raise Exception("You have to provide the name of the table...")
        sql = f"""select * from {sys.argv[1]}"""
        for result in handler.execute(sql):
            print(result)
#commentselect * from register_set_map2

  

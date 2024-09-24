from sys import getsizeof
import oracledb
oracledb.init_oracle_client()

un = 'ecal_p2ug_conf'
dns = 'int2r-s.cern.ch:10121/int2r_lb.cern.ch'
import getpass
pw =  getpass.getpass('\nInsert DB password: ')

threshold_value = 1

with oracledb.connect(user=un, password=pw, dsn=dns) as connection:
    with connection.cursor() as handler:
        sql = """DELETE FROM register_sets WHERE register_set_id > :1"""
        handler.execute(sql, [threshold_value])
        connection.commit()

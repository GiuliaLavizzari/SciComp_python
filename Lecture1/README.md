# Python interface to ORACLE DB for CMS ECAL Phase-2 Upgrade

## Installation instructions

Extra package installed with pip:
```shell
python -m pip install oracledb --upgrade --user
```

You also need to update the LD_LIBRARY_PATH as follows:
```shell
export LD_LIBRARY_PATH=/home/daqpro/dbrpc/apx-prime/rpcclient/rpcsvc_client_dev:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/home/daqpro/anaconda3/envs/dbrpc/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/home/daqpro/dbrpc/apx-prime/rpcclient/rpcsvc_client_dev:$LD_LIBRARY_PATH
```

This can be added in the conda activation script, eg:
```shell
 /home/<user>/anaconda3/envs/<conda-env>/etc/conda/activate.d/env_vars.sh
```

NB: this works in `dbrpc` and `rogue_5.9.3` environments

## Simple usage example
```python
from DbInterface import DbInterface
dbi = DbInterface(username, password, dsn)
    
register_set_id = dbi.uploadRegisterSetFromJson("all_registers.json", "test from class")
thisdict = dbi.getJsonFromRegisterSet(register_set_id)
```

### Structure
Help on DbInterface in module DbInterface object:
```
class DbInterface(builtins.object)
 |  DbInterface(un, pw, dsn)
 |
 |  Methods defined here:
 |
 |  __del__(self)
 |
 |  __init__(self, un, pw, dsn)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  addRegister(self, register_type_id, device_key, register)
 |
 |  addRegisterSet(self, notes='Default')
 |
 |  addToSetMap(self, register_set_id, register_id)
 |
 |  commit(self)
 |
 |  getJsonFromRegisterSet(self, register_set_id)
 |
 |  getRegisterTypeId(self, device_type, address)
 |
 |  uploadRegisterSetFromJson(self, inputjson, notes)
 |
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  connection = None
 |  handler = None
```

## Additional scripts
Few additional utilities in the scripts folder, they allow for example for printing a db table or deleting rows.

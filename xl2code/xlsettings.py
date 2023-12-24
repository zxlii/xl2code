import atexit
import json
import logging
from pathlib import Path
from attr import asdict, dataclass

@dataclass
class Xlsettings:
    input:str           = ""
    output:str          = ""
    lang:str            = "lua"
    type:str            = "code"
    data:str            = ""
    _instance           = None
    
    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kw)
        return cls._instance

    def __post_init__(self):

        config_file = Path("settins.json")
        if config_file.exists():
            try:
                with open(config_file) as f:
                    json_data = json.loads(f.read())
                    self.__dict__.update(json_data)
            except Exception as err:
                pass
        else:
            logging.warn("config file '{}' not exists. well using defautl values .".format(config_file))

        # 程序退出时保存配置到配置文件 /tmp/config.json
        def sync_to_disk():
            json_str = json.dumps(asdict(self), indent=4)
            with open(config_file, 'w') as f:
                logging.warning("save configs to '{}' ".format(config_file))
                f.write(json_str) 
        atexit.register(sync_to_disk)
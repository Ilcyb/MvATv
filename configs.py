from os.path import dirname, join
from mvatv.aria2 import aria2_config_file_path

all_configs = ('aria2_path')

need_read_configs = ('save_path', 'plugins_path')

aria2_path = 'aria2c' # default path of aria2

aria2_config_path = aria2_config_file_path()
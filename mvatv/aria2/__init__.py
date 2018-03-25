from os.path import dirname, join, abspath

def aria2_config_file_path():
    return abspath(join(dirname(__file__), 'aria2.config'))

def aria2_tracker_file_path():
    return abspath(join(dirname(__file__), '.tracker'))

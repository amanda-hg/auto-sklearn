import os
from get_logger import logger

def get_folder_structure(root_path="./", config_fname="config.json"):
    """Gets and checks the paths the execution folder strucutre. The names of the folder
        are a conventiong. Please don't modify them.
    Args:
        root_path (str, optional): root path of the folder stcuture. Defaults to ./
        config_fname (str, optional): config filename. Defaults to config.json
    Returns:
        (str): dir_output, dir_tmp, config_path
    """
    if not isinstance(root_path, str):
        raise TypeError("root_path must be str")
    if not isinstance(config_fname, str):
        raise TypeError("config_fname must be str")
    dir_output = os.path.join(root_path, "output/")
    dir_tmp = os.path.join(root_path, "tmp/")
    config_path = os.path.join(root_path, "config/", config_fname)
    dir_output = os.path.normpath(dir_output)
    dir_tmp = os.path.normpath(dir_tmp)
    config_path = os.path.normpath(config_path)
    if not os.path.isdir(dir_output):
        raise Exception("path of output data does not exist: {}".format(dir_output))
    if not os.path.isdir(dir_tmp):
        raise Exception("path of tmp data does not exist: {}".format(dir_tmp))
    if not os.path.isfile(config_path):
        logger.info("there is no config file")
        config_path = None
    return dir_output, dir_tmp, config_path
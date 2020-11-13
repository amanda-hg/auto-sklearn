"""This module handles all the input/output of the main workflow.
workflow version: 1.0.0
"""

import time
import os

# MODULES
from global_vars import ROOT_PATH, CONFIG_NAME
from config import get_schema, read_config, validate_config
from get_logger import config_logger, logger
from utils import get_folder_structure

######### SOURCE CODE #########
config_logger(ROOT_PATH)
time_start = time.time()
current_time = time.strftime("%Y-%m-%d %H:%M:%S %Z", time.gmtime(time_start))
logger.info("Execution started at "+current_time)

# Get paths
dir_output, dir_tmp, config_path = get_folder_structure(root_path=ROOT_PATH, \
                                                        config_fname=CONFIG_NAME)

print(dir_output)
print(dir_tmp)
print(config_path)

logger.info("Validation config file..")
# Load config
schema = get_schema()
config = read_config(config_path=config_path)
config = validate_config(config=config, schema=schema)

print(config)
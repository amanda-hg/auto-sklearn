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
from regression import train_regression, predict_regression
from classification import train_classification, predict_classification
from multi_label import train_multi_label, predict_multi_label

######### SOURCE CODE #########
config_logger(ROOT_PATH)
time_start = time.time()
current_time = time.strftime("%Y-%m-%d %H:%M:%S %Z", time.gmtime(time_start))
logger.info("Execution started at "+current_time)

# Get paths
dir_model, dir_output, dir_tmp, config_path = get_folder_structure(root_path=ROOT_PATH, \
                                                                   config_fname=CONFIG_NAME)
logger.info("Validation config file..")
# Load config
schema = get_schema()
config = read_config(config_path=config_path)
config = validate_config(config=config, schema=schema)

# If its TRAIN and PREDICT
if config['train'] and config['predict']:
    # Regression model
    if config['model_type'] == 'regression':
        train_regression(dir_model, dir_tmp, dir_output)
        predict_regression(dir_model, dir_output)

    # Classification model
    if config['model_type'] == 'classification':
        train_classification(dir_model, dir_tmp, dir_output)
        predict_classification(dir_model, dir_output)

    # Multi-label model
    if config['model_type'] == 'multi-label':
        train_multi_label(dir_model, dir_tmp, dir_output)
        predict_multi_label(dir_model, dir_output)

# If its just PREDICTION
if (not config['train']) and (config['predict']):
    # Regression model
    if config['model_type'] == 'regression':
        predict_regression(dir_model, dir_output)
    # Classification model
    if config['model_type'] == 'classification':
        predict_classification(dir_model, dir_output)
    # Multi-label model
    if config['model_type'] == 'multi-label':
        predict_multi_label(dir_model, dir_output)

time_end = time.time()
duration_time = time.strftime("%Hh %Mm %Ss", time.gmtime(time_end-time_start))
logger.debug("Execution ended at " + duration_time)
logger.info("Execution ended at " + duration_time)
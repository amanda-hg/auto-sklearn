import os
import time
import sklearn.datasets
import sklearn.metrics
import autosklearn.regression

from get_logger import logger
from save_output import save_pickle

def train_regression(dir_model, dir_tmp, dir_output):
    """Validates with cerberus the config file agains the schema.
    Args:
        dir_tmp (string): The temporal folder path.
        dir_output (string): The output folder path.
    Returns:
        automl (Regression): The regression model.
    """
    try:
        time1 = time.time()
        time_exec = time.strftime("%Y%m%d", time.gmtime(time1))

        tmp_folder = os.path.join(dir_tmp, 'autosklearn_regression_example_tmp_'+time_exec)
        output_folder = os.path.join(dir_output, 'autosklearn_regression_example_out_'+time_exec)
        print(tmp_folder)
        print(output_folder)

        # Load a example dataset
        X, Y = sklearn.datasets.load_boston(return_X_y=True)
        X_train, X_test, Y_train, Y_test = sklearn.model_selection.train_test_split(X, Y, random_state=1)

        # Create regression model
        automl = autosklearn.regression.AutoSklearnRegressor(time_left_for_this_task=120,
                                                            per_run_time_limit=30,
                                                            tmp_folder=tmp_folder,
                                                            output_folder=output_folder)

        logger.info('Training the regression model..')
        # Train model
        automl.fit(X_train, Y_train, dataset_name='boston')
        logger.info('Save the regression model..')
        # Save for the prediction
        save_pickle(automl, "regression_model", dir_model)
        return automl
    
    except ValueError as error:
        print(error)
        exit(1)

def predict_regression(dir_model, dir_output):
    pass
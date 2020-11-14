import os
import time
import pickle
import sklearn.datasets
import sklearn.metrics
import autosklearn.regression

from get_logger import logger
from save_output import save_pickle, save_txt

def train_regression(dir_model, dir_tmp, dir_output):
    """Train a Regression model with autosklearn.
    Args:
        dir_tmp (string): The temporal folder path.
        dir_output (string): The output folder path.
    Returns:
        void
    """
    time1 = time.time()
    time_exec = time.strftime("%Y%m%d", time.gmtime(time1))

    tmp_folder = os.path.join(dir_tmp, 'autosklearn_regression_example_tmp_'+time_exec)
    output_folder = os.path.join(dir_output, 'autosklearn_regression_example_out_'+time_exec)

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
    save_pickle(automl, "regression_model", dir_model)
    # Save test
    save_pickle(X_test, "x_test", dir_model)
    save_pickle(Y_test, "y_test", dir_model)

def predict_regression(dir_model, dir_output):
    """Predict a Regression model
    Args:
        dir_model (string): The model folder path.
        dir_output (string): The output folder path.
    Returns:
        void
    """
    try:
        automl = pickle.load(open(os.path.join(dir_model, 'regression_model.p'), "rb" ))
    except:
        logger.error('There is not model to predict.')
        exit(1)
    
    x_test = pickle.load(open(os.path.join(dir_model, 'x_test.p'), "rb" ))
    y_test = pickle.load(open(os.path.join(dir_model, 'y_test.p'), "rb" ))
    # Calculate predictions
    predictions = automl.predict(x_test)
    # Calculate stadistics
    r2_score = sklearn.metrics.r2_score(y_test, predictions)
    # Save stats
    save_txt(r2_score, 'R2_score', dir_output)


import os
import time
import pickle
import sklearn.datasets
import sklearn.metrics
import autosklearn.classification

from get_logger import logger
from save_output import save_pickle, save_txt

def train_classification(dir_model, dir_tmp, dir_output):
    """Train a classification model.
    Args:
        dir_tmp (string): The temporal folder path.
        dir_output (string): The output folder path.
    Returns:
        automl (Regression): The regression model.
    """
    time1 = time.time()
    time_exec = time.strftime("%Y%m%d", time.gmtime(time1))
    tmp_folder = os.path.join(dir_tmp, 'autosklearn_classification_example_tmp_'+time_exec)
    output_folder = os.path.join(dir_output, 'autosklearn_classification_example_out_'+time_exec)

    # Load a example dataset
    X, Y = sklearn.datasets.load_breast_cancer(return_X_y=True)
    X_train, X_test, Y_train, Y_test = sklearn.model_selection.train_test_split(X, Y, random_state=1)

    # Create classification model
    automl = autosklearn.classification.AutoSklearnClassifier(time_left_for_this_task=120,
                                                                per_run_time_limit=30,
                                                                tmp_folder=tmp_folder,
                                                                output_folder=output_folder)

    logger.info('Training the classification model..')
    # Train model
    automl.fit(X_train, Y_train, dataset_name='breast_cancer')
    logger.info('Save the classification model..')
    save_pickle(automl, "classification_model", dir_model)
    # Save test
    save_pickle(X_test, "x_test", dir_model)
    save_pickle(Y_test, "y_test", dir_model)

def predict_classification(dir_model, dir_output):
    """Predict a Regression model
    Args:
        dir_model (string): The model folder path.
        dir_output (string): The output folder path.
    Returns:
        void
    """
    try:
        automl = pickle.load(open(os.path.join(dir_model, 'classification_model.p'), "rb" ))
    except:
        logger.error('There is not model to predict.')
        exit(1)
    
    x_test = pickle.load(open(os.path.join(dir_model, 'x_test.p'), "rb" ))
    y_test = pickle.load(open(os.path.join(dir_model, 'y_test.p'), "rb" ))
    # Calculate predictions
    predictions = automl.predict(x_test)
    # Calculate stadistics
    accuracy_score = sklearn.metrics.accuracy_score(y_test, predictions)
    # Save stats
    save_txt(accuracy_score, 'Acuraccy_score', dir_output)
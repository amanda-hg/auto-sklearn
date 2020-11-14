import os
import pickle
import numpy as np
import sklearn.datasets
import sklearn.metrics
from sklearn.utils.multiclass import type_of_target
import autosklearn.classification

from get_logger import logger
from save_output import save_pickle, save_txt

def train_multi_label(dir_model, dir_tmp, dir_output):
    """Train a Multi label classification model
    Args:
        dir_tmp (string): The temporal folder path.
        dir_output (string): The output folder path.
    Returns:
        automl (Regression): The regression model.
    """
    # Load a example dataset
    X, Y = sklearn.datasets.fetch_openml(data_id=40594, return_X_y=True, as_frame=False)

    # "Positive classes are indicated with 1 and negative classes with 0 or -1."
    # More information on: https://scikit-learn.org/stable/modules/multiclass.html
    Y[Y == 'TRUE'] = 1
    Y[Y == 'FALSE'] = 0
    Y = Y.astype(np.int)

    print(f"type_of_target={type_of_target(Y)}")
    X_train, X_test, Y_train, Y_test = sklearn.model_selection.train_test_split(X, Y, random_state=1)

    # Create multi_label model
    automl = autosklearn.classification.AutoSklearnClassifier(time_left_for_this_task=60,
                                                                per_run_time_limit=30,
                                                                # Bellow two flags are provided to speed up calculations
                                                                # Not recommended for a real implementation
                                                                initial_configurations_via_metalearning=0,
                                                                smac_scenario_args={'runcount_limit': 1})

    logger.info('Training the multi_label model..')
    # Train model
    automl.fit(X_train, Y_train, dataset_name='reuters')

    logger.info('Save the multi_label model..')
    save_pickle(automl, "multi_label_model", dir_model)
    # Save test
    save_pickle(X_test, "x_test", dir_model)
    save_pickle(Y_test, "y_test", dir_model)

def predict_multi_label(dir_model, dir_output):
    """Predict a Multi-label classification model
    Args:
        dir_model (string): The model folder path.
        dir_output (string): The output folder path.
    Returns:
        void
    """
    try:
        automl = pickle.load(open(os.path.join(dir_model, 'multi_label_model.p'), "rb" ))
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
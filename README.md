<center><u><h1>auto-sklearn</h1></u></center>

## 1. Index

1. Index
2. Installation
3. Introduction
4. Description
5. Folder structure
6. Execution
    * 6.1 Configuration file
7. Output

## 2. Installation
The dependences needed for the auto-sklearn installation on Mac OSX: 

1) Press Command+Space and type Terminal and press enter/return key.
2) Run in Terminal app:
    ```curl https://raw.githubusercontent.com/automl/auto-sklearn/master/requirements.txt | xargs -n 1 -L 1 pip3 install``` 
3) Finally run:
    ```pip3 install auto-sklearn```

#### Anaconda
A common installation problem under recent Linux distribution is the incompatibility of the compiler version used to compile the Python binary shipped by AnaConda and the compiler installed by the distribution. This can be solved by installing the gcc compiler shipped with AnaConda (as well as swig):
``` conda install gxx_linux-64 gcc_linux-64 swig```

## 3. Introduction
This module teach about use auto-sklearn Python library. 
The main objective of auto-sklearn is to free the user from the selection of the algorithm, and from the search and optimization of hyperparameters. The library is based on the most recent advances in Bayesian optimization, meta-learning, and ensemble construction.

## 4. Description
In this application we are gonna execute three differents model with Auto-sklearn: \
* Regression
* Classifcation
* Multi-label Classification

When the user executes this application, the model executed is gonna save in the *model* folder. This model will be readed for the prediction. When the prediction has made, the application will save some stadistics about our model in the *output* folder.
For run this application, the user has to configurate a file situated in the *config* folder. That file is the *config.json*

In the *logs* folder will be save two logs. The *logfile.log* what is the official user logs and the *debug.log* that is the internal logs.

There is a *notebooks* folder where it keeps three notebooks, one for each model. Besides, each notebook has different graphs for represent the stadistics of the model. This is a good experience for a begginer user in the caculate of model because the notebook is fully configurable.

## 5. Folder structure

```python
auto-sklearn
    |
    |-------- config/
    |           |-------- config.file
    |
    |-------- code/
    |
    |-------- logs/
    |
    |-------- model/
    |
    |-------- output/
    |
    |-------- tmp/
```
**IMPORTANT:**
**For the application to work you must respect this folder structure.**

## 6. Execution
In this parts, we are gonna to explain how execute this application. 

### 6.1 Configuration file
The *config.file* has three configurable fields: 
```python
{
    "model_type": "String of model to execute. It allows three options: 'regression', 'classification' 'multi-label'",
    "train": "Boolean value. If its true, the model will be trained.",
    "predict": "Boolean value. If its true, the model will be predicted and the results will be saved.",
}
```

## 7. Output
The results of this application is the stadistics of the model selected. They will be saved in a text file.
The output can be a R2 score file or Accuray file. Both will name like their stadistics name.
The output file will be in the output folder and it will be overwrite if the user doesn't rename it.

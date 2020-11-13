<center><u><h1>auto-sklearn</h1></u></center>

## 1. Index

1. Index
2. Installation
3. Introduction
4. Description
5. Folder structure
6. Execution
    * 5.1 Configuration file
    * 5.2 Input data
7. Results
    * 7.1 Output
    * 7.2 Output example

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


## 5. Folder structure

```python
auto-sklearn
    |
    |-------- data/
    |             |-------- input-dataset.csv
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

For the application to work you must respect this folder structure.
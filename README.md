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
    ```ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" < /dev/null 2> /dev/null``` 
    and press enter/return key.
    If the screen prompts you to enter a password, please enter your Mac's user password to continue. When you type the password, it won't be displayed on screen, but the system would accept it. So just type your password and press ENTER/RETURN key. Then wait for the command to finish.
3) Run:
    ```brew install swig```
4) Run:
    ```pip install auto-skelarn``

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
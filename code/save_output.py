import os
import pickle
import time

def save_pickle(obj_to_save, filename, path_to_save):
    ''' Method to save objects as pickle
    Parameters:
        -obj_to_save (object)
        -filename (string)
        -path_to_save (string)
    '''
    fname = os.path.join(path_to_save, filename+".p")
    pickle.dump(obj_to_save, open(fname, "wb"))

def save_txt(text, filename, path_to_save):
    ''' Method to save objects as pickle
    Parameters:
        -obj_to_save (object)
        -filename (string)
        -path_to_save (string)
    '''
    fname = os.path.join(path_to_save, filename)
    file1 = open(fname,"w") 
    file1.write(text)
    file1.close()
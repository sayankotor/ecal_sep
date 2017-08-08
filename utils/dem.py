import pickle
#from hep_ml.reweight import BinsReweighter
import numpy as np
from sklearn import preprocessing
from sklearn.cross_validation import train_test_split

def rev_(X_train):
    X_train_rev = list()
    for elem in X_train:
        X_train_rev.append(elem.ravel())
    X_train_rev = np.array(X_train_rev)
    return X_train_rev

def conc(x): return np.concatenate((x[0], x[1]), axis=0) 

def write_data(str1, str2):
    with open(str1) as f_in:
        X1, hypo1, y1, energy1 = pickle.load(f_in)

    with open(str2) as f_in:
        X2, hypo2, y2, energy2 = pickle.load(f_in)
    return np.array(X1), np.array(hypo1), np.array(y1), np.array(energy1), np.array(X2), np.array(hypo2), np.array(y2), np.array(energy2)

def write_data2(str_):
    with open(str_) as f_in:
        square, square_reconstruct, y, y_reconstruct, area, area_reconstruct = pickle.load(f_in)
    print "area list len:", len(area), len(area_reconstruct)
    return np.array(square), np.array(y), np.array(area), np.array(square_reconstruct), np.array(y_reconstruct), np.array(area_reconstruct)


def preprocess2(str1, str2):
    square_1, y1, area1, square_reconstruct1, y_reconstruct1, area_reconstruct1 =  write_data2(str1)
    square_2, y2, area2, square_reconstruct2, y_reconstruct2, area_reconstruct2 =  write_data2(str2)    
    list1 = write_data2(str1)
    list2 =  write_data2(str2)

    squares, y, area,squares_reconstr, y_reconsrt, area_reconstr = map(conc, zip(list1, list2))
    
    ret1 =  train_test_split(squares, y, area)
    ret2 =  train_test_split(squares_reconstr, y_reconsrt, area_reconstr)
    return ret1, ret2

def write_data3(str_):
    with open(str_) as f_in:
        square_All, square_inner, square_outer, y, y_inner, y_outer, area_list, area_list_inner, area_list_outer = pickle.load(f_in)
    print "area list len:", len(area_list), len(area_list_inner), len(area_list_outer)
    return [np.array(square_All), np.array(y), np.array(area_list), np.array(square_inner), np.array(y_inner), np.array(area_list_inner), np.array(square_outer), np.array(y_outer), np.array(area_list_outer)]

def preprocess3(str1, str2):
    list1 = write_data3(str1)
    list2 =  write_data3(str2)

    squares, y, area,squares_inner, y_inner, area_inner, squares_outer, y_outer, area_outer = map(conc, zip(list1, list2))

    ret1 =  train_test_split(squares, y, area)
    ret2 =  train_test_split(squares_inner, y_inner, area_inner)
    ret3 =  train_test_split(squares_outer, y_outer, area_outer)
    
    return ret1, ret2, ret3

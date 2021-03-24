#!/usr/bin/env python3

import numpy as np

def data_spliter(x, y, proportion):
    if type(proportion) != float or type(x) != np.ndarray or y.ndim != 1\
        or len(y) == 0 or type(y) != np.ndarray or x.shape[0] != y.shape[0]:
        return None
    if x.ndim == 1:
        X = np.concatenate((y.reshape(len(y), 1), x.reshape(len(x), 1)),
            axis=1)
    else:
         X = np.concatenate((y.reshape(len(y), 1), x), axis=1)
    X = np.random.permutation(X)
    prop = int(proportion * len(y))
    a = np.hsplit(X, np.array([1, len(y)]))
    train =(X[:prop,:])
    test = (X[prop:,:])
    ret_train = np.hsplit(train, np.array([1, len(y)]))
    ret_test = np.hsplit(test, np.array([1, len(y)]))
    return ret_train[1].transpose(), ret_test[1].transpose(),\
        ret_train[0].transpose(), ret_test[0].transpose()


if __name__ == "__main__":
    x1 = np.array([1, 42, 300, 10, 59])
    y = np.array([1, 2, 3, 4, 5])
    x2 = np.array([ [ 1, 42],
    [300, 10],
    [ 59, 1],
    [300, 59],
    [ 10, 42]])
    print("1")
    a = data_spliter(x1, y, 0.5)
    print(a[0])
    print(a[1])
    print(a[2])
    print(a[3])
    print("2")
    a = (data_spliter(x1, y, 0.5))
    print(a[0])
    print(a[1])
    print(a[2])
    print(a[3])
    print("3")
    a = (data_spliter(x2, y, 0.8))
    print(a[0])
    print(a[1])
    print(a[2])
    print(a[3])

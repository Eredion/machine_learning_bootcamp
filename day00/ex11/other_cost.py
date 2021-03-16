#! /usr/bin/env python3

import numpy as np
import math


def mse_(y, y_hat):
    if type(y_hat) != np.ndarray or type(y) != np.ndarray or y.ndim != 1\
            or y_hat.ndim != 1 or len(y_hat) != len(y):
        return None
    else:
        return(np.dot((1 / (len(y)))*(y_hat - y), (y_hat - y)))


def rmse_(y, y_hat):
    ret = mse_(y, y_hat)
    if ret is None:
        return ret
    else:
        return (math.sqrt(ret))


def mae_(y, y_hat):
    if type(y_hat) != np.ndarray or type(y) != np.ndarray or y.ndim != 1\
            or y_hat.ndim != 1 or len(y_hat) != len(y):
        return None
    else:
        return(np.sum((abs((y_hat - y))/len(y))))


def r2score_(y, y_hat):
    if type(y_hat) != np.ndarray or type(y) != np.ndarray or y.ndim != 1\
            or y_hat.ndim != 1 or len(y_hat) != len(y):
        return None
    else:
        return 1.0 - (np.sum((y_hat - y) ** 2) / np.sum((y - np.mean(y)) ** 2))


if __name__ == "__main__":
    X = np.array([0, 15, -9, 7, 12, 3, -21])
    Y = np.array([2, 14, -13, 5, 12, 4, -19])
    X2 = np.array([8, 15, 0, 7, 16, 3, -2])
    Y2 = np.array([-2, 15, -13, 5, -12, 34, -19])

    print(mse_(X, Y))
    print(rmse_(X, Y))
    print(mae_(X, Y))
    print(r2score_(X, Y))


    

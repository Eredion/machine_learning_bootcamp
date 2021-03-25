#!/usr/bin/env python3

import numpy as np


def add_intercept(x):
    if len(x) < 1 or type(x) != np.ndarray:
        return None
    return(np.c_[np.ones(x.shape[0]), x])


def logistic_predict(x, theta):
    if len(x) < 1 or type(x) != np.ndarray or type(theta) != np.ndarray or\
            len(theta) < 1:
        return None
    X = add_intercept(x)
    try:
        return (1 / (1 + np.exp(-X @ theta)))
    except:
        return None

if __name__ == "__main__":
    x = np.array([4])
    x2 = np.array([[4], [7.16], [3.2], [9.37], [0.56]])
    x3 = np.array([[0, 2, 3, 4], [2, 4, 5, 5], [1, 3, 2, 7]])
    theta = np.array([[2], [0.5]])
    theta2 = np.array([2, 0.5])
    print(logistic_predict(x, theta))
    theta2 = np.array([[2], [0.5]])
    print(logistic_predict(x2, theta2))
    theta3 = np.array([[-2.4], [-1.5], [0.3], [-1.4], [0.7]])
    print(logistic_predict(x3, theta3))

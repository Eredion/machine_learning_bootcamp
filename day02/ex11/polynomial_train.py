#!/usr/bin/env python3

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def add_polynomial_features(x, power):
    if type(x) != np.ndarray or len(x) == 0 or type(power) != int or\
            x.ndim != 1 or power < 1:
        return None
    ret = []
    for i in range(len(x)):
        y = []
        for j in range(power):
            y.append(x[i] ** (j + 1))
        ret.append(y)
    return (np.array(ret))


def gradient(x, y, theta):
    if type(x) != np.ndarray or type(y) != np.ndarray or len(x) == 0 or\
            len(y) == 0 or type(theta) != np.ndarray or len(theta) == 0 or\
            y.shape[0] != x.shape[0] or x.shape[1] != (theta.shape[0] - 1):
        return None
    X = np.insert(x, 0, 1.0, axis=1)
    y_hat = X @ theta
    J = ((y_hat - y) @ X)/len(x)
    return (J)


def fit_(x, y, theta, alpha=0.005, n_cycles=5000):
    if type(x) != np.ndarray or type(y) != np.ndarray or len(x) == 0 or\
            len(y) == 0 or type(theta) != np.ndarray or len(theta) == 0 or\
            y.shape[0] != x.shape[0] or x.shape[1] != (theta.shape[0] - 1) or\
            type(alpha) != float or type(n_cycles) != int or n_cycles < 0:
        return None
    theta = np.array(theta, dtype=np.float128)
    for i in range(n_cycles):
        J = gradient(x, y, theta)
        for c in range(len(theta)):
            theta[c] = theta[c] - alpha * J[c]
    return(theta)


def simple_predict(x, theta):
    if type(x) != np.ndarray or type(theta) != np.ndarray or len(x) == 0\
            or x.shape[1] != (theta.shape[0] - 1):
        return None
    X = np.insert(x, 0, 1.0, axis=1)
    y_hat = X @ theta
    return(y_hat)


def cost_(y, y_hat):
    if type(y_hat) != np.ndarray or type(y) != np.ndarray or y.ndim != 1\
            or y_hat.ndim != 1 or len(y_hat) != len(y):
        return None
    else:
        return(np.dot((1 / (len(y)))*(y_hat - y), (y_hat - y)))

if __name__ == "__main__":
    data = np.asarray(pd.read_csv('are_blue_pills_magics.csv')).transpose()
    x = data[1]
    y = data[2]
    x = (x - np.mean(x))/np.std(x)
    y = (y - np.mean(y))/np.std(y)
    cont_x = np.arange(-2, 2.01, 0.01)
    t1 = fit_(add_polynomial_features(x, 1), y, np.array([1., 1.]))
    y1 = simple_predict(x.reshape(-1, 1), t1)
    cost1 = cost_(y, y1)
    ts = []
    costs = []
    for i in range(1, 9):
        ones = np.ones((i + 1,), dtype=float)
        t = fit_(add_polynomial_features(x, i), y, ones)
        y_hat = simple_predict(add_polynomial_features(x, i), t)
        cost = cost_(y, y_hat)
        costs.append(cost)
        ts.append(t)
    print(costs)
    plt.bar(list(range(2, 10)), costs, color='orange')
    plt.show()




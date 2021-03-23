#!/usr/bin/env python3

import numpy as np


def simple_predict(x, theta):
    if type(x) != np.ndarray or type(theta) != np.ndarray or len(x) == 0\
            or x.shape[1] != (theta.shape[0] - 1):
        return None
    y_hat = []
    for i in range(x.shape[0]):
        y = theta[0]
        for j in range(x.shape[1]):
            y += x[i][j] * theta[j + 1]
        y_hat.append(y)
    return y_hat


if __name__ == "__main__":
    x = np.arange(1, 13).reshape((4, 3))
    theta1 = np.array([5, 0, 0, 0])
    print(simple_predict(x, theta1))
    theta2 = np.array([0, 1, 0, 0])
    print(simple_predict(x, theta2))
    theta3 = np.array([-1.5, 0.6, 2.3, 1.98])
    print(simple_predict(x, theta3))
    theta4 = np.array([-3, 1, 2, 3.5])
    print(simple_predict(x, theta4))

#!/usr/bin/env python3

import numpy as np

def gradient(x, y, theta):
    if type(x) != np.ndarray or type(y) != np.ndarray or len(x) == 0 or\
        len(y) == 0 or type(theta) != np.ndarray or len(theta) == 0 or\
        y.shape[0] != x.shape[0] or x.shape[1] != (theta.shape[0] - 1):
        return None
    X = np.insert(x, 0, 1.0, axis=1)
    y_hat = X @ theta
    J = ((y_hat - y) @ X)/len(x)
    return (J)

if __name__ == '__main__':
    x = np.array([
    [ -6, -7, -9],
    [ 13, -2, 14],
    [ -7, 14, -1],
    [ -8, -4, 6],
    [ -5, -9, 6],
    [ 1, -5, 11],
    [ 9, -11, 8]])
    y = np.array([2, 14, -13, 5, 12, 4, -19])
    theta1 = np.array([3, 0.5,-6, 1])

    print(gradient(x, y, theta1))
    theta2 = np.array([0, 0, 0, 0])
    print(gradient(x, y, theta2))

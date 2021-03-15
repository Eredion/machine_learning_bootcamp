#! /usr/bin/env python3

import numpy as np

def cost_(y, y_hat):
    if type(y_hat) != np.ndarray or type(y) != np.ndarray or y.ndim != 1\
            or y_hat.ndim != 1 or len(y_hat) != len(y):
        return None
    else:
        return(np.dot((1 / (2 * len(y)))*(y_hat - y) ,(y_hat - y)))


if __name__ == "__main__":
    X = np.array([0, 15, -9, 7, 12, 3, -21])
    Y = np.array([2, 14, -13, 5, 12, 4, -19])

    print(cost_(X, Y))
    print(cost_(X, X))

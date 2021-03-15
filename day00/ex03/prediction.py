#! /usr/bin/env python3

import numpy as np


def simple_predict(x, theta):
    if type(theta) != np.ndarray or type(x) != np.ndarray or x.ndim != 1\
            or theta.ndim != 1 or len(theta) != 2:
        return None
    else:
        y_hat = []
        for i in x:
            y_hat.append(theta[0] + i * theta[1])
        return (y_hat)

if __name__ == "__main__":
    x = np.arange(1, 6)
    theta1 = np.array([5, 0])
    print(simple_predict(x, theta1))

    theta2 = np.array([0, 1])
    print(simple_predict(x, theta2))

    theta3 = np.array([5, 3])
    print(simple_predict(x, theta3))

    theta4 = np.array([-3, 1])
    print(simple_predict(x, theta4))

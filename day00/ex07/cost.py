#! /usr/bin/env python3

import numpy as np


def add_intercept(x):
    if type(x) == np.ndarray and x.size > 0 and x.ndim == 1:
        y = np.ones(x.size,)
        return(np.array([y, x]).transpose())
    else:
        return (None)


def predict(x, theta):
    if type(theta) != np.ndarray or type(x) != np.ndarray or x.ndim != 1\
            or theta.ndim != 1 or len(theta) != 2:
        return None
    else:
        x = add_intercept(x)
        return (x @ theta)


def cost_elem_(y, y_hat):
	if type(y_hat) != np.ndarray or type(y) != np.ndarray or y.ndim != 1\
            or y_hat.ndim != 1 or len(y_hat) != len(y):
		return None
	else:
		return((1 / (2 * len(y)))*(y_hat - y) * (y_hat - y))

def cost_(y, y_hat):
    ret = cost_elem_(y, y_hat)
    if ret is not None:
        return(sum(ret))
    else:
        return None


if __name__ == "__main__":
    x1 = np.array([0., 1., 2., 3., 4.])
    theta1 = np.array([2., 4.])
    y_hat1 = predict(x1, theta1)
    y1 = np.array([2., 7., 12., 17., 22.])
    print(cost_elem_(y1, y_hat1))
    print(cost_(y1, y_hat1))

    x3 = np.array([0, 15, -9, 7, 12, 3, -21])
    theta3 = np.array([0., 1.])
    y_hat3 = predict(x3, theta3)
    y3 = np.array([2, 14, -13, 5, 12, 4, -19])
    print(cost_(y3, y_hat3))
    print(cost_(y3, y3))

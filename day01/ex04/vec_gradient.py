#! /usr/bin/env python3

import numpy as np


def simple_gradient(x, y, theta):
    if type(theta) != np.ndarray or type(x) != np.ndarray or x.ndim != 1\
            or theta.ndim != 1 or len(theta) != 2 or type(y) != np.ndarray\
            or y.ndim != 1 or len(y) != len(x):
        return None
    else:
        X = np.concatenate(((np.ones((len(x), 1))), x.reshape(len(x), 1)),
                           axis=1)
        h0 = X @ theta
        J = ((h0 - y) @ X)/len(x)
        return(abs(J))

if __name__ == "__main__":
    print("Hola")
    x = np.array([12.4956442, 21.5007972, 31.5527382, 48.9145838, 57.5088733])
    y = np.array([37.4013816, 36.1473236, 45.7655287, 46.6793434, 59.5585554])
    
    theta1 = np.array([2, 0.7])
    print(simple_gradient(x, y, theta1))
    
    theta2 = np.array([1, -0.4])
    print(simple_gradient(x, y, theta2))

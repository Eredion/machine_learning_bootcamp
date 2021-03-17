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
        return((J))

def fit_(x, y, theta, alpha, max_iter):
    if type(theta) != np.ndarray or type(x) != np.ndarray or x.ndim != 1\
            or theta.ndim != 1 or len(theta) != 2 or type(y) != np.ndarray\
            or y.ndim != 1 or len(y) != len(x) or type(alpha) != float or\
        type(max_iter) != int or max_iter < 0 :
        print((x.ndim))
        print((y.ndim))
        print((theta.ndim))
        return None
    else:
        new_theta = np.array([float(theta[0]), float(theta[1])])
        for i in range(max_iter):
            J = simple_gradient(x, y, new_theta)
            new_theta[0] = new_theta[0] - alpha * J[0]
            new_theta[1] = new_theta[1] - alpha * J[1]
        return(new_theta)



if __name__ == "__main__":
    x = np.array([12.4956442, 21.5007972, 31.5527382, 48.9145838, 57.5088733])
    y = np.array([37.4013816, 36.1473236, 45.7655287, 46.6793434, 59.5585554])
    theta= np.array([1, 1])
    theta1 = fit_(x, y, theta, alpha=5e-8, max_iter = 1500000)
    print(theta1)


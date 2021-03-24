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

def fit_(x, y, thetha, alpha, n_cycles):
    if type(x) != np.ndarray or type(y) != np.ndarray or len(x) == 0 or\
        len(y) == 0 or type(theta) != np.ndarray or len(theta) == 0 or\
        y.shape[0] != x.shape[0] or x.shape[1] != (theta.shape[0] - 1) or\
        type(alpha) != float or type(n_cycles) != int or n_cycles < 0:
        return None
    for i in range(n_cycles):
        J = gradient(x, y, theta)
        for c in range(len(theta)):
            theta[c] = theta[c] - alpha * J[c]
    return(theta)

if __name__ == '__main__':
    x = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8., 80.]])
    y = np.array([19.6, -2.8, -25.2, -47.6])
    theta = np.array([42., 1., 1., 1.])
    theta2 = fit_(x, y, theta, alpha = 0.0005, n_cycles=42000)
    print(theta2)



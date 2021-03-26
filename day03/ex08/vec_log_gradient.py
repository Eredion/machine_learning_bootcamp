#!/usr/bin/env python3

import numpy as np
from log_pred import logistic_predict
from log_pred import add_intercept
from vec_log_loss import log_loss_

def vec_log_gradient(x, y, theta):
    h0 = logistic_predict(x, theta)
    J = 1 / len(y) * (add_intercept(x).transpose() @ (h0 - y))
    return (J)


if __name__ == "__main__":
    y1 = np.array([1])
    x1 = np.array([4])
    theta1 = np.array([[2], [0.5]])
    print(vec_log_gradient(x1, y1, theta1))
    y2 = np.array([[1], [0], [1], [0], [1]])
    x2 = np.array([[4], [7.16], [3.2], [9.37], [0.56]])
    theta2 = np.array([[2], [0.5]])
    print(vec_log_gradient(x2, y2, theta2))
    y3 = np.array([[0], [1], [1]])
    x3 = np.array([[0, 2, 3, 4], [2, 4, 5, 5], [1, 3, 2, 7]])
    theta3 = np.array([[-2.4], [-1.5], [0.3], [-1.4], [0.7]])
    print(vec_log_gradient(x3, y3, theta3))


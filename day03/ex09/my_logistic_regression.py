#!/usr/bin/env pyrhon3

import numpy as np
import matplotlib.pyplot as plt

class MyLogisticRegression():
    def __init__(self,  thetas, alpha=0.1, max_iter=1000):
        self.alpha = alpha
        self.max_iter = max_iter
        self.thetas = thetas

    def gradient(self, x, y):
        if len(x) < 1 or len(y) < 1 or len(self.thetas) < 1 or x is None or y is None or self.thetas is None or x.shape[0] != y.shape[0]:
            return None
        y_hat = self.predict_(x)
        gr_vec = ((np.transpose(self.add_intercept(x)) @ (y_hat - y))) / y.shape[0]
        return gr_vec

    def fit_(self, x, y):
        if len(x) < 1 or len(y) < 1 or len(self.thetas) < 1 or x.shape[0] != y.shape[0] or x is None or y is None:
            return None
        for _ in range(self.max_iter):
            self.thetas -= (self.gradient(x, y) * self.alpha)
        return self.thetas

    def predict_(self, x):
        if len(x) < 1 or len(self.thetas) < 1 or x is None or self.thetas is None:
            return None
        return 1 / (1 + np.exp(- self.add_intercept(x) @ self.thetas))

    def add_intercept(self, x):
        if len(x) < 1 or type(x) is not np.ndarray:
            return None
        return np.c_[np.ones(x.shape[0]), x]

    def cost_(self, y_hat, y, eps=1e-15):
        return -(1 / y.shape[0]) * np.sum((y * np.log(y_hat + eps)) + (1 - y) * np.log(1 - y_hat + eps))

if __name__ == "__main__":
    X = np.array([[1., 1., 2., 3.], [5., 8., 13., 21.], [3., 5., 9., 14.]])
    Y = np.array([[1], [0], [1]])
    mylr = MyLogisticRegression([[2], [0.5], [7.1], [-4.3], [2.09]])

    print(mylr.predict_(X))
    print(mylr.cost_(mylr.predict_(X), Y))

    mylr.fit_(X, Y)
    print(mylr.thetas)

    print(mylr.predict_(X))
    print(mylr.cost_(mylr.predict_(X), Y))

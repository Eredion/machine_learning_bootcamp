#! /usr/bin/env python3

import numpy as np


class MyLinearRegression():
    def __init__(self, thetas, alpha=0.001, n_cycle=1000):
        try:
            if type(alpha) != float or type(n_cycle) != int or alpha < 0 or\
               n_cycle < 0 or len(thetas) != 2 or type(thetas) != np.ndarray:
                    raise ValueError
            self.alpha = alpha
            self.max_iter = n_cycle
            self.thetas = thetas
        except ValueError:
            exit("Error: Wrong MyLinearRegression initialization.")

    def simple_gradient(self, x, y, theta):
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

    def fit_(self, x, y):
        if type(x) != np.ndarray or x.ndim != 1 or type(y) != np.ndarray\
                or y.ndim != 1 or len(y) != len(x):
            return None
        new_theta = np.array([float(self.thetas[0]), float(self.thetas[1])])
        for i in range(self.max_iter):
            J = self.simple_gradient(x, y, new_theta)
            new_theta[0] = new_theta[0] - self.alpha * J[0]
            new_theta[1] = new_theta[1] - self.alpha * J[1]
        self.thetas = new_theta
        return(new_theta)

    def predict_(self, x):
        if type(x) != np.ndarray or x.ndim != 1:
            return None
        X = np.concatenate(((np.ones((len(x), 1))), x.reshape(len(x), 1)),
                           axis=1)
        h0 = X @ self.thetas
        return(h0)

    def cost_elem_(self, x, y):
        if type(x) != np.ndarray or x.ndim != 1 or type(y) != np.ndarray\
                or y.ndim != 1 or len(y) != len(x):
            return None
        h0 = self.predict_(x)
        return((1 / (2 * len(y)))*(h0 - y) * (h0 - y))

    def cost_(self, x, y):
        if type(x) != np.ndarray or x.ndim != 1 or type(y) != np.ndarray\
                or y.ndim != 1 or len(y) != len(x):
            return None
        return(sum(self.cost_elem_(x, y)))


if __name__ == "__main__":
    x = np.array([12.4956442, 21.5007972, 31.5527382, 48.9145838, 57.5088733])
    y = np.array([37.4013816, 36.1473236, 45.7655287, 46.6793434, 59.5585554])
    lr1 = MyLinearRegression(np.array([2, 0.7]))
    
    print(lr1.predict_(x))
    print(lr1.cost_elem_(lr1.predict_(x), y))
    print(lr1.cost_(lr1.predict_(x), y))

    lr2 = MyLinearRegression(np.array([0., 0.]))

    print(lr2.fit_(x, y))
    print(lr2.predict_(x))
    print(lr2.cost_elem_(lr1.predict_(x),y))
    print(lr2.cost_(lr1.predict_(x),y))


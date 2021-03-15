#! /usr/bin/env python3

import numpy as np
from matplotlib import pyplot as plt


def plot(x,  y, theta):
    if type(theta) != np.ndarray or type(x) != np.ndarray or x.ndim != 1\
            or theta.ndim != 1 or len(theta) != 2 or type(y) != np.ndarray\
            or y.ndim != 1 or len(y) != len(x):
        return None
    else:
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(x, y, 'o')
        ax.plot(x, theta[1]*x + theta[0])
        plt.show()

if __name__ == "__main__":
    x = np.arange(1, 6)
    y = np.array([3.74013816, 3.61473236, 4.57655287, 4.66793434, 5.95585554])
    theta1 = np.array([4.5, -0.2])
    plot(x, y, theta1)

    theta2 = np.array([-1.5, 2])
    plot(x, y, theta2)

    theta3 = np.array([3, 0.3])
    plot(x, y, theta3)

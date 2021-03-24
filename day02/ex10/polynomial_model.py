#!/usr/bin/env python3

import numpy as np


def add_polynomial_features(x, power):
    if type(x) != np.ndarray or len(x) == 0 or type(power) != int or\
            x.ndim != 1 or power < 1:
        return None
    ret = []
    for i in range(len(x)):
        y = []
        for j in range(power):
            y.append(x[i] ** (j + 1))
        ret.append(y)
    return (np.array(ret))


if __name__ == "__main__":
    x = np.arange(1, 6)
    print(x)
    print(add_polynomial_features(x, 3))
    print(add_polynomial_features(x, 6))

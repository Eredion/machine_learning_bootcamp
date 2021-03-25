#!/usr/bin/env python3

import numpy as np
import math


def sigmoid_(x):
    if type(x) != np.ndarray or x.size == 0:
        return None
    x = x.astype(float)
    if x.size == 1:
        return (1/(1 + math.exp(-x)))
    if x.ndim > 1:
        try:
            x = x.transpose().reshape(-1)
        except:
            return None
    for i in range(x.size):
        n = (1/(1 + math.exp(-x[i])))
        x[i] = n
    return x

if __name__ == "__main__":
    print(sigmoid_(np.array(-4)))
    print(sigmoid_(np.array(2)))
    print(sigmoid_(np.array([[-4], [2], [0]])))
    print(sigmoid_(np.array([-4, 2, 0])))

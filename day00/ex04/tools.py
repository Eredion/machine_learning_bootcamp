#! /usr/bin/env python3
import numpy as np


def add_intercept(x):
    if type(x) == np.ndarray and x.size > 0 and x.ndim == 1:
        y = np.ones(x.size,)
        return(np.array([y, x]).transpose())
    else:
        return (None)


if __name__ == "__main__":
    x = np.arange(1, 6)
    print(add_intercept(x))

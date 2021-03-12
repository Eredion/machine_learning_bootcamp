#! /usr/bin/env python3

import numpy as np


class Vector:
    def __init__(self, arg):
        try:
            self.values = []
            if isinstance(arg, int):
                self.size = arg
                for i in range(arg):
                    self.values.append(float(i))
            elif isinstance(arg, list):
                self.size = len(arg)
                for i in arg:
                    if isinstance(i, float) is False:
                        raise(ValueError)
                    self.values = arg
            elif isinstance(arg, tuple) and len(arg) == 2:
                for i in range(arg[0], arg[1]):
                            self.values.append(float(i))
                            self.size = len(self.values)
            else:
                raise(ValueError)
        except ValueError:
            exit("Error: Wrong vector initialization")

    def __str__(self):
        return (f"Vector values: {self.values}")

    def __repr__(self):
        return (f"Vector size: {self.size}\nVector values: {self.values}")


"""
    def __add__

    def __radd__

    def __sub__

    def __rsub__

    def __truediv__

    def __rtruediv__

    def __mul__

    def __rmul__

    def __str__

    def __repr__
"""


print(Vector(8))
print(Vector([1.0, 2.3, 4.5]))
print(Vector((10,15)))
print(type(Vector(8)))
a = np.ones(5)
print(a)
print(a + 5)

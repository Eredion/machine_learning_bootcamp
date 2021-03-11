#! /usr/bin/env python3

print(type(5))
print(type((1, 3)))
print(type([1, 2, 3]))


class Vector:
    def __init__(self, arg):
        if isinstance(arg, int):
            self.size = arg
            self.values = range(0, (arg))

    def __str__(self):
        return (f"Vector size: {self.size}\nVector values: {self.values}\n")
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

v = Vector(3)
print(v)

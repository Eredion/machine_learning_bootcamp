#! /usr/bin/env python3


class Vector:
    def __init__(self, arg1, arg2=None):
        if arg2 != None and isinstance(arg1, int) and isinstance(arg2, int) and arg2 > arg1:
            ret = 3
        elif isinstance(arg1, int) == True and arg2 == None and arg1 > 0:
            ret = 2
        elif isinstance(arg1, list) and arg2 == None:
            ret = 1
            for elem in arg1:
                if isinstance(elem, float) == False:
                    ret = 0
        else:
            ret = 0
        if ret == 0:
            exit("ERROR: invalid inicialization of Vector class")
        elif ret == 1:
            self.values = arg1
        elif ret == 2:
            self.values = []
            for i in range(0, arg1):
                self.values.append(float(i))
        elif ret == 3:
            self.values = []
            for i in range(arg1, arg2):
                self.values.append(float(i))
        self.size = len(self.values)

    def __str__(self):
        txt = '(Vector ' + str(self.values) + ')'
        return txt

    def __repr__(self):
        txt = 'Vector values: ' + str(self.values) + '\nVector size: ' + str(self.size)
        return txt

    def __add__(self, n):
        new_value = []
        if isinstance(n, int) or isinstance(n, float):
            for i in range(0, self.size):
                new_value.append(self.values[i] + n)
        elif isinstance(n, Vector) and n.size == self.size:
            for i in range(0, self.size):
                new_value.append(self.values[i] + n.values[i])
        else:
            exit("ERROR: invalid sum")
        return Vector(new_value)

    def __radd__(self, n):
        return (self + n)

    def __sub__(self, n):
        new_value = []
        if isinstance(n, int) or isinstance(n, float):
            for i in range(0, self.size):
                new_value.append(self.values[i] - n)
        elif isinstance(n, Vector) and n.size == self.size:
            for i in range(0, self.size):
                new_value.append(self.values[i] - n.values[i])
        else:
            exit("ERROR: invalid substraction")
        return Vector(new_value)

    def __rsub__(self, n):
        return ((self * -1) + n)

    def __mul__(self, n):
        if isinstance(n, int) or isinstance(n, float):
            new_value = []
            for i in range(0, self.size):
                new_value.append(self.values[i] * n)
            ret = Vector(new_value)
        elif isinstance(n, Vector) and n.size == self.size:
            ret = 0
            for i in range(0, self.size):
                ret += (self.values[i] * n.values[i])
        else:
            exit("ERROR: invalid multiplication")
        return ret

    def __rmul__(self, n):
        return (self * n)
        
    def __truediv__(self, n):
        if isinstance(n, int) or isinstance(n, float):
            if n == 0:
                exit("ERROR: division by 0")
            new_value = []
            for i in range(0, self.size):
                new_value.append(self.values[i] / n)
            ret = Vector(new_value)
        else:
            exit("ERROR: invalid division")
        return ret

    def __rtruediv__(self, n):
        if isinstance(n, int) or isinstance(n, float):
            if n == 0:
                exit("ERROR: division by 0")
            new_value = []
            for i in range(0, self.size):
                new_value.append(n / self.values[i])
            ret = Vector(new_value)
        else:
            exit("ERROR: invalid division")
        return ret

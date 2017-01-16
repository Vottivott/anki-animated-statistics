import numbers

class Vector:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return "(%.1f, %.1f)" % (self.x, self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        if ( isinstance(scalar, numbers.Number)):
            return Vector(self.x * scalar, self.y * scalar)
        raise TypeError("can't multiply Vector by non-numeric type")

    def __div__(self, scalar):
        if ( isinstance(scalar, numbers.Number)):
            return Vector(self.x / scalar, self.y / scalar)
        raise TypeError("can't multiply Vector by non-numeric type")

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


if __name__ == "__main__":
    v = Vector(1,2)
    w = Vector(10,1.5)
    print v*2
import math

class Shape:
    def area(self):
        raise NotImplementedError
    def perimeter(self):
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def age(self, value):
        self._radius = value

    def area(self):
        return math.pi * self._radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self._radius


class Square(Shape):
    def __init__(self, side_length):
        self._side_length = side_length

    @property
    def side_length(self):
        return self._side_length

    @side_length.setter
    def side_length(self, value):
        self._side_length = value

    def area(self):
        return self._side_length ** 2

    def perimeter(self):
        return 4 * self._side_length
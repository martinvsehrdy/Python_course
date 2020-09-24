from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def length(self):
        pass

    @abstractmethod
    def expand(self):
        pass

class Circle(Shape):
    def __init__(self, center_x, center_y, radius):
        self._center_x = center_x
        self._center_y = center_y
        self._radius = radius

    def area(self):
        return pi * self._radius

    def length(self):
        return 2 * self._radius

    def expand(self):
        pass
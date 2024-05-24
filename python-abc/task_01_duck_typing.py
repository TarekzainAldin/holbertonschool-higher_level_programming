#!/usr/bin/env python3

from abc import ABC, abstractmethod
import math


#   Shape abs class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# S Implement
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# shape info function
def shape_info(shape):
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))


# Test
if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 6)

    print("Circle info:")
    shape_info(circle)
    print()

    print("Rectangle info:")
    shape_info(rectangle)

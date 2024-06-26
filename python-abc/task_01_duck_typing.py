#!user/bin/env python3
"""abs class """

from abc import ABC, abstractmethod
import math


# Shape Abstract Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# Circle Class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# Rectangle Class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# shape_info Function
def shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


# Testing the shape_info function with Circle and Rectangle
circle = Circle(5)
rectangle = Rectangle(4, 7)

print("Circle Info:")
shape_info(circle)

print("\nRectangle Info:")
shape_info(rectangle)

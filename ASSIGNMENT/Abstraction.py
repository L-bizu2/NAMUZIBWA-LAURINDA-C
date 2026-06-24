from abc import ABC, abstractmethod

import math


class Shape(ABC):

    """Abstract base class representing a generic geometric shape."""

    @abstractmethod

    def area(self):

        pass


    @abstractmethod

    def perimeter(self):

        pass



class Rectangle(Shape):

   
    def __init__(self, length, width):

        self.length = length

        self.width = width


    def area(self):

        return self.length * self.width


    def perimeter(self):

        return 2 * (self.length + self.width)


class Circle(Shape):


    def __init__(self, radius):

        self.radius = radius


    def area(self):

        return math.pi * (self.radius ** 2)


    def perimeter(self):

        return 2 * math.pi * self.radius



print("=== Geometric Shapes Abstraction Test ===")


# 1. Instantiating and testing the Rectangle

print("\n--- Testing Rectangle ---")

my_rectangle = Rectangle(length=10, width=5)

print(f"Rectangle Area: {my_rectangle.area():.2f}")

print(f"Rectangle Perimeter: {my_rectangle.perimeter():.2f}")



# 2. Instantiating and testing the Circle

print("\n--- Testing Circle ---")

my_circle = Circle(radius=7)

print(f"Circle Area: {my_circle.area():.2f}")

print(f"Circle Circumference (Perimeter): {my_circle.perimeter():.2f}")

print("=========================================")



# test_shape = Shape() will throw a TypeError 
# because you cannot create an instance of an abstract class directly!

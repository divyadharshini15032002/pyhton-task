from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculateArea(self):
        pass
    @abstractmethod
    def calculateperimeter(self):
        pass

class Circles(Shape):
    def __init__(self,radius):
        self.radius = radius
    def calculateArea(self):
        return math.pi * self.radius ** 2
    def calculateperimeter(self):
        return 2 * math.pi * self.radius
    

class Triangle(Shape):
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def calculateperimeter(self):
        return self.a + self.b + self.c
    def calculateArea(self):
        s= self.calculateperimeter() /2
        area = math.sqrt(s*(s-self.a) * (s-self.b)*(s-self.c))
        return area
    print()

circle = Circles(5)
triangle = Triangle(3,6,8)

print("Circles")
print("Area:",circle.calculateArea())
print("perimeter:",circle.calculateperimeter())
print()
print("Triangle")
print("Area:",triangle.calculateArea())
print("perimeter:",triangle.calculateperimeter())





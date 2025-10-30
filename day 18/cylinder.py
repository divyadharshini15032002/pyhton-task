from abc import ABC,abstractmethod
import math

class Shapes(ABC):
    @abstractmethod
    def volume(self):
        pass

class Cylinder(Shapes):
    def __init__(self,radius,height):
        self.radius = radius
        self.height = height
    def volume(self):
        return math.pi * self.radius ** 2 * self.height

class Cones(Shapes):
    def __init__(self,radius,height):
        self.radius = radius
        self.height = height
    def volume(self):
        return (1/3) * math.pi * self.radius ** 2 * self.height

class Shaper(Shapes):
    def __init__(self,radius):
        self.radius = radius
    def volume(self):
        return (4/3) * math.pi * self.radius ** 3

cylinder = Cylinder(3,8)
cone = Cones(3,8)
shaper = Shaper(5)

print("Cylinder")
print("volume:",cylinder.volume())
print()

print("Cones")
print("voiume:",cone.volume())
print()

print("Shaper")
print("volume:",shaper.volume())
      
    
    

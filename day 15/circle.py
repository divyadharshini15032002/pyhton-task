import math
class Circle:
    
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        "Return the area of the circle."
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        "Return the perimeter(circumference) of the circle"
        return 2 * math.pi * self.radius
    
    r = float(input("enter the radius of the circle:"))
    c = Circle(r)

    print(f"area of the circle:{c.area():.2f}")
    print(f"perimeter of the circle:{c.perimeter():.2f}")

import math
class Shape:
    
    def area(self):
        pass
    def perimeter(self):
        pass

class Circle(Shape):
        
        def __init__(self, radius):
            self.radius = radius
        def area(self):
            return math.pi * self.radius ** 2
        def perimeter(self):
            return 2 *math.pi *self.radius

class Triangle(Shape):
    
        def __int__(self, a, b, c, height=None):
            self.a = a
            self. b = b
            self. c = c
            self.height = height

        def area(self):
            if self.height is not None:
                return 0.5 * self.b * self.height
            else:
                s=(self.a + self.b + self.c)/2
                return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        def perimeter(self):
            return self.a + self.b + self.c

class Square(Shape):
    
        def __init__(self, side):
            self.side = side

        def area(self):
            return self.side ** 2

        def perimeter(self):
            return 4 * self.side

print("Choose a shape: circle,triangle,square")
choice = input("Enter shape name:").strip().lower()

if choice == "circle":
    r=float(input("Enter radius:"))
    c = Circle(r)
    print(f"Area: {c.area():.2f}")
    print(f"perimeter:{c.perimeter():.2f}")

elif choice == "triangle":
        a = float(input("Enter side a:"))
        b = float(input("Enter side b:"))
        c = float(input("Enter side c:"))
        use_hight = input("Do you want to use height for area calculation? (y/n):").lower()
        if use_height == "y":
            h = float(input("Enter height corresponding to base b:"))
            t = Triangle(a, b, c, h)
        else:
            t = Triangle(a, b, c)
            print(f"Area: {t.area():.2f}")
            print(f"Perimeter: {t.perimeter():.2f}")

elif choice == "square":
    a = float(input("Enter side length:"))
    s = Square(a)
    print(f"Area: {s.area():>2f}")
    print(f"Perimeter: {s.perimeter():.2f}")

else:
    print("Invalid shape choice.")
        

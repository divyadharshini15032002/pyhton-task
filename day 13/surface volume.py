import math
h=float(input("Enter a hight surface volume:"))
r=float(input("Enter a radius surface volume:"))
volume= math.pi * r ** 2 * h
surface_area = (2 * math.pi * r * h) + (2 * math.pi * r ** 2)
print(volume)
print(surface_area)

try:
    a = int(input("enter the first number:"))
    b = int(input("enter the second number:"))
    if(a<0,orb<0):
        raise TypeError("Ngative value are not allowed")
except ValueError:
    print("please give valid input")
    

class calculator:
    def add (self, a,b):
        return a+b
    def sub(self, a,b):
        return a-b
    def mul(self, a,b):
        return a*b
    def div(self, a,b):
        return a/b
    
calc=calculator()

a=float(input("Enter a first number:"))
b=float(input("Enter a second number:"))

print("Addition",calc.add(23,6))
print("Subtraction",calc.sub(23,6))
print("Multiplication",calc.mul(23,6))
print("Division",calc.div(23,6))
        
        

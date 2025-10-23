def simple_calculator(a,b, operator):
    if operator == '+':
        result = a+b
    elif operator == '-':
        result = a-b
    elif operator == '*':
        result = a*b
    elif operator == '/':
        if b !=0:
            result = a/b
        else:
                return"Error: Division by zero!"
    else:
                return "Invalid operator! use +,-,* or /"
            
    return f"The result of {a} {operator} {b} = {result}"
print(simple_calculator(10,5,'+'))
print(simple_calculator(10,5,'-'))
print(simple_calculator(10,5,'*'))
print(simple_calculator(10,5,'/'))
                

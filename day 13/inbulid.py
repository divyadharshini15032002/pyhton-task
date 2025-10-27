n=int(input("Enter the values of n:"))
r=int(input("Enter the values of r:"))
def factorial(num):
    result = 1
    for i in range(1,num+ 1):
        result *= i
        return result
ncr= factorial(n)/(factorial(r)*factorial(n - r))
print(ncr)

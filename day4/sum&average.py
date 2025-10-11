sum=0
print("The first 10 natural numbers are:")
for number in range(1,11):
    print(number,end="")
    sum+=number
    print("\nsum of the numbers:",sum)
    average=sum/10
    print("Average of the numbers:",average)
    

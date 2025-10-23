def sum_numbers(*args):
    print("The sum of all number is:",sum(args))
nums=list(map(int, input("enter a number of sperated space:").split()))
sum_numbers(*nums)

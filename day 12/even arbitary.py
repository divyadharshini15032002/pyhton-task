def even_numbers(*a):
    print("Even numbers from the given list are:")
    for num in a:
        if num % 2 == 0:
            print(num, end= " ")
even_numbers(5,8,9,5,3,2,1)

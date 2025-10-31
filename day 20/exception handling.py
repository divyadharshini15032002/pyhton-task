try:
   a= int(input("enter a first nmber"))
   b = int(input("enter a second number"))
   c=a/b
   

   print("A value is",a)
   print("B value is",b)
   print("Division Value",c)

except ZeroDivisionError:
    print("Division by zero  is not allowed")

except ValueError:
    print("please enter valid numeric values!")

except Exception as e:
    print("enter a division number")

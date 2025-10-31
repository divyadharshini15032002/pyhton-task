try:
   a= int(input("enter a first nmber"))
   b = int(input("enter a second number"))
   c=a+b
   

   print("A value is",a)
   print("B value is",b)
   print("Add Value",c)

except TypeError:
    print("invalid data type provide")

except ValueError:
    print("please enter valid numeric values!")

except Exception as e:
    print("enter a division number")

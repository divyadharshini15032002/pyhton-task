from simple_calc import add,sub,mul,div
from date_today import today_date

try:
    a = float(input("enter the A value:"))
    b = float(input("enter the B value:"))

    print("\n1.Addition 2.Subtraction 3.Multiplication 4.Division")
    choice = int(input("Enter the choice to perfrom:"))

    if choice == 1:
       result = add(a,b)
       operation = "Addition"
       
    elif choice == 1:
        result = sub(a,b)
        operation = "Subtraction"

    elif choice == 2:
        result = sub(a,b)
        operation = "Multiplication"

    elif choice == 3:
        result = mul(a,b)
        operation = "Division"

    else:
        raise ValueError("invalid choice entered!")


except ValueError as ve:
    print (f"Value Error: {ve}")
except ZeroDivisionError as zde:
    print (f"Math Error: {zde}")
except Exception as e:
    print(f"Unexcepted Error: {e}")

else:
    date_info = today_date().strftime("%d %B %Y %A")
    print(f"\nDate:{date_info}")
    print (f"{operation} of two numbers: {result}")
finally:
    print("\n thank you for using simplr calculator!")
    

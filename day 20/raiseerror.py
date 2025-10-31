try:
  a= int(input("enter a value:"))
  b= int(input("enter second value:"))
  if(a<0 or b<0):
    raise  TypeError ("please enter a valid numerical value.")
  else:
    c=a*b
    print("you have to pay",c)
except ValueError:
    print("please give valid number")
    
    


    

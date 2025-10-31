try:
  a = int(input("enter an integer:"))
  if not value.isdigit():
    raise ValueError ("it is not valid:")
  else:
    print("value is =", int (value))

except ValueError as e:
    
    print("e")

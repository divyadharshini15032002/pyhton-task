from datetime import datetime
date_string=input("Enter a date and time(format: 'YYYY-MM-DD HH:MM:SS'):" )
date_object = datetime.strptime(date_string,'%Y-%m-%d %H:%M:%S')
print(date_object)
print("Type of varible:",type(date_object))

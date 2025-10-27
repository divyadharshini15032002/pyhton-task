import datetime 
now = datetime.datetime.now()
print("Time tuple current date and time",now.timetuple())
print("Time tuple year,y[0]):",now.timetuple()[0])
print("Time Tuple month of year",("y[1]"), now.timetuple()[1])
print("Week number of the year",now.strftime("%U"))
print("weekday of the week",now.strftime("%w"))
print("day of year",now.strftime("%j"))
print("Time tuple day of  month(y[2]):",now.timetuple()[2])
print(" Day of week(y[6]):",now.timetuple()[6])


from datetime import datetime
date_string = "July 1 14 2:43PM"
object= datetime.strptime(date_string, "%B %d %y %I:%M%p")
print(object)

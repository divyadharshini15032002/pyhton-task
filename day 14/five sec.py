from datetime import datetime,timedelta
current_time = datetime.now()
new_time = current_time + timedelta(seconds=5)
print("current time:",current_time)
print("time after 5 seconds",new_time)


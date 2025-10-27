from datetime import date,timedelta
current_date = date.today()
new_date = current_date - timedelta(days=5)
print("current date:",current_date)
print("5 days before current date:",new_date)

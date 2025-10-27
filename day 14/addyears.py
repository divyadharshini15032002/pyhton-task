import datetime
def addyears(d, years):
    try:
        return d.replace(year=d.year + years)
    except valueError:
        return d.replace(month=2, day=28, year=d.year + years)
print(addyears(datetime.date(2015,1,1),-1))
print(addyears(datetime.date(2015,1,1),0))
print(addyears(datetime.date(2015,1,1),2))
print(addyears(datetime.date(2000,2,29),1))
               

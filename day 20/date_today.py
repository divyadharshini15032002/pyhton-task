from datetime import datetime,timedelta
def today_date():
    return datetime.now()
def yesterday():
    return datetime.now() - timedelta(days=1)
def tomorrow():
    return datetime.now() + timedelta(days=1)

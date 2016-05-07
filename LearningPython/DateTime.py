#import pytz
import datetime
import date

def time_diff(timestamp1, timestamp2):
    td = timestamp1 - timestamp2
    return round(abs(td.days * 1440 + td.seconds/60))

def get_age(birth_date, current_date = None):
    if(current_date is None ):
        current_date = datetime.datetime.utcnow()

    return current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))

def is_leap_year(year):
    if(year % 4 != 0):
        return False
    elif(year % 100 != 0):
        return True
    elif(year % 400 != 0):
        return False
    else:
        return True

#def future_datetime(timestamp, unit, delta):
#    if(unit == "seconds"):
#        return timestamp + timedelta(seconds: delta)
#    elif(unit == "minutes"):
#    elif(unit == "hours"):
#    elif(unit == "days"):
#    elif(unit == "weeks"):
#    elif(unit == "months"):  
#    elif(unit == "years"):  


f = datetime.datetime(1987, 11, 4, 19, 39, 7)
s = datetime.datetime(1983, 5, 13, 9, 42, 40)

print(get_age(datetime.datetime(1991,8,20)))
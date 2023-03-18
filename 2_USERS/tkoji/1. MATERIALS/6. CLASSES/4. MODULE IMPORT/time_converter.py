# function display date
# function display time
# funtion time diff

import datetime as dt

time_now = dt.datetime.now()

def display_date(date):
    date_user_obj = dt.datetime.strptime(date, '%d.%m.%Y')
    new = date_user_obj.strftime('%d.%m.%Y %H%M%S')
    return new

def display_time(time):
    date_user_obj = dt.datetime.strptime(time, '%d.%m.%Y')
    date_user_obj.strftime('%d.%m.%Y %H%M%S')
    return date_user_obj

def display_time_diff(arg1, arg2):
    date_user_obj = dt.datetime.strptime(arg2, '%d.%m.%Y')
    diff = arg1 - date_user_obj
    return diff

#user_date = input("Please input the date in fromat dd.mm.year: ")
user_date = '21.12.2012'

print(display_date(user_date))
print(display_time(user_date))
print(display_time_diff(time_now, user_date))
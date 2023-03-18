from calendar import weekday
import datetime as dt
import locale
from dateutil import relativedelta, FR
from dateutil import tz

today = dt.date.today() 
print(today)

time_now = dt.datetime.now()
print(time_now)

set_time = dt.time(12,30,00,111)
print(set_time)

week_day = dt.date.weekday(today)  # 5 because 
print(week_day)

print(time_now.strftime('%A'))
print(time_now.strftime('%c'))


locale.setlocale(locale.LC_TIME, 'hr_HR')
print(time_now.strftime('%A'))


locale.setlocale(locale.LC_TIME, 'de_DE')
print(time_now.strftime('%A'))

# Last Friday in a month
last_friday = relativedelta(day=31, weekday=FR(-1))
print(last_friday)
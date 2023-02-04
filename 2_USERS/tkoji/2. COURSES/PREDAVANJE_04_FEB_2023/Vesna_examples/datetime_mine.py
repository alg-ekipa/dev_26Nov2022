import datetime as dt

print(dt.datetime.today())
hour = dt.datetime.now().hour
minute = dt.datetime.now().minute
year = dt.datetime.now().year

print(f'The time is {hour}h passed {minute} minutes.')
import datetime as dt

# tdate = dt.datetime(2000, 11, 25, 12, 0, 1)
# print(tdate.strftime('%d.%m.%Y'))

# date_object = dt.datetime.strptime('20.04.2022', '%d.%m.%Y')
# print(date_object)

# date_user = input('Input date in fromat dd.mm.yyyy ')

# date_user_obj = dt.datetime.strptime(date_user, '%d.%m.%Y')
# print(date_user_obj.date())


date_user1 = input('Input date in fromat (Month dd yyyy) ')
date_user_obj = dt.datetime.strptime(date_user1, '%b %d %Y')
print(date_user_obj.date())


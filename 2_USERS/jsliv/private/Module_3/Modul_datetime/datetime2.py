import datetime as dt
from dateutil.relativedelta import relativedelta, FR
from dateutil import tz

sadasnji_treuntak = dt.datetime.now()
neki_datum = dt.datetime(2020,10,5,12,0,0)
danas= dt.date.today()

print("Sadasnji trenutak:", sadasnji_treuntak)
print("Neki datum: ", neki_datum)

print("Razlika između ", sadasnji_treuntak - neki_datum)
print()
za_14_dana = sadasnji_treuntak + dt.timedelta(days=14, hours=10)
print(za_14_dana)
print("Jucer", danas - dt.timedelta(days=1))
print("Sutra", danas + dt.timedelta(days=1))

#Koji je zadnji petak u mjesecu?

zadnji_petak = relativedelta(day = 31, weekday = FR(-1))
print(zadnji_petak)

tz_zg = tz.gettz("Zagreb")
termin_zg = dt.datetime(2021,3,29, tzinfo=tz_zg)
print("ZG", termin_zg)

tz_ny = tz.gettz("NewYork")
termin_ny = termin_zg.astimezone(tz_ny)
print("NY",termin_ny)

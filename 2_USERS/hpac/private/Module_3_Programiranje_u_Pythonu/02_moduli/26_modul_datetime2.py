import datetime as dt
from dateutil.relativedelta import relativedelta, FR
from dateutil import tz

sadasnji_trenutak = dt.datetime.now()
neki_datum = dt.datetime(2020, 1, 27, 12, 52, 5)
danas = dt.date.today()

print('Sadašnji trenutak', sadasnji_trenutak)
print('Neki datum', neki_datum)

print('Razlika između ta dva datuma: ', (sadasnji_trenutak - neki_datum)/365)

za_14_dana = sadasnji_trenutak + dt.timedelta(days=14)
print(za_14_dana)

print('Jučer:', danas - dt.timedelta(days=1))
print('Sutra:', danas + dt.timedelta(days=1))

# KOji datum je zadnji petak u mjesecu?
#zadnji_petak = relativedelta(day=31, weekday=FR(-1))
#print(zadnji_petak)

# Vremenske zone

tz_zg = tz.gettz('Europe/Zagreb')
termin_zg = dt.datetime(2021, 3, 29, tzinfo=tz_zg)
print('ZG',termin_zg)
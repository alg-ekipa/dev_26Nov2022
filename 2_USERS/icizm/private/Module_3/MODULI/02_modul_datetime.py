import datetime as dt
from dateutil.relativedelta import relativedelta, FR
from dateutil import tz

sadasnji_trenutak =dt.datetime.now()
neki_datum = dt.datetime(2020, 10, 5, 12, 0 , 0)
danas = dt.date.today()

print('Sadašnji trenutak: ', sadasnji_trenutak)
print('Sadašnji trenutak: ', neki_datum)

print('Razlika između ta dva datuma/trenutka:', sadasnji_trenutak-neki_datum) # izbaci razliku u danima, satima itd

# da smo uzeli samo dva datuma izbacilo bi razliku samo u danima

za_14_dana = sadasnji_trenutak + dt.timedelta(days=14, hours=10)
print(za_14_dana)

print('Jučer:', danas - dt.timedelta(days=1))
print('Sutra:', danas + dt.timedelta(days=1))

# Koji datum je zadnji petak u mjesecu?

zadnji_petak = relativedelta(day = 31, weekday=FR(-1))
print(zadnji_petak)

import datetime as dt
from dateutil.relativedelta import relativedelta, FR
from dateutil import tz

sadasnji_trenutak =dt.datetime.now()
neki_datum = dt.datetime(2020, 10, 5, 12, 0 , 0)
danas = dt.date.today()

print('Sadašnji trenutak: ', sadasnji_trenutak)
print('Sadašnji trenutak: ', neki_datum)

print('Razlika između ta dva datuma/trenutka:', sadasnji_trenutak-neki_datum) # izbaci razliku u danima, satima itd
print()

# da smo uzeli samo dva datuma izbacilo bi razliku samo u danima

za_14_dana = sadasnji_trenutak + dt.timedelta(days=14, hours=10) 
print('Za 14 dana će biti: ',za_14_dana)
print()

print('Jučer:', danas - dt.timedelta(days=1))
print('Sutra:', danas + dt.timedelta(days=1))
print()

# Koji datum je zadnji petak u mjesecu?

zadnji_petak = relativedelta(day = 31, weekday=FR(-1))
print(zadnji_petak)
print()


# Vremenske zone 


tz_zg = tz.gettz('Europe/Zagreb')
termin_zg = dt.datetime(2021, 3, 29, tzinfo=tz_zg)
print('ZG', termin_zg)
print()

tz_ny = tz.gettz('America/New_York')
termin_ny = termin_zg.astimezone(tz_ny)
print('NY', termin_ny)
print()

tz_la = tz.gettz('America/Los_Angeles')
termin_la = termin_zg.astimezone(tz_la)
print('LA', termin_la)
print()

tz_hk = tz.gettz('Asia/Hong_Kong')
termin_hk = termin_zg.astimezone(tz_hk)
print('NY', termin_hk)
print()
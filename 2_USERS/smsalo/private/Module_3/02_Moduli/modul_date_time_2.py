import datetime as dt
from dateutil.relativedelta import relativedelta, FR
from dateutil import tz


sadasnji_trenutak=dt.datetime.now()
neki_datum=dt.datetime(2020,10,5,12,0,0)
danas=dt.date.today()

print('Sadašnji trenutak: ', sadasnji_trenutak)
print('neki datum:', neki_datum)

print('Razlika između ta dva datuma/trenutka: ', (sadasnji_trenutak-neki_datum) )

za_14_dana=sadasnji_trenutak+dt.timedelta(days=14, hours=10)
print(za_14_dana)

print('Jučer: ', danas - dt.timedelta(days=1))
print('Sutra: ', danas + dt.timedelta(days=1))


# koji datum je zadnji petak u mjesecu?
zadnji_petak = relativedelta(day=31, weekday=FR(-1))
print(zadnji_petak)

#vremenske zone

tz_zg = tz.gettz('Europe/Zagreb')
termin_zg = dt.datetime(2021, 3, 29, tzinfo=tz_zg)

tz_ny = tz.gettz('America/New_York')
termin_ny = termin_zg.astimezone(tz_ny)

tz_la = tz.gettz('America/Los_Angeles')
termin_la = termin_zg.astimezone(tz_la)

tz_hk = tz.gettz('Asia/Hong_Kong')
termin_hk = termin_zg.astimezone(tz_hk)

print(f'Termin u Zagrebu pocinje u {termin_zg.strftime("%A %d.%m.%Y. %H:%M")}')
print(f'Termin u New Yorku pocinje u {termin_ny.strftime("%A %d.%m.%Y. %H:%M")}')
print(f'Termin u Los Angelesu pocinje u {termin_la.strftime("%A %d.%m.%Y. %H:%M")}')
print(f'Termin u Hong Kongu pocinje u {termin_hk.strftime("%A %d.%m.%Y. %H:%M")}')

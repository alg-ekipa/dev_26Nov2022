import datetime as dt
import locale

danas = dt.date.today() #danasnji datum YYYY-MM-DD
print(danas)

sada = dt.datetime.now() #sadasnji trenutak
print(sada)

sada_vrijeme = dt.time(12,30,0) # vrijeme kreirano preko parametara koje prenosimo
print(sada_vrijeme)

dan = dt.date.weekday(danas) # vraca broj 0-6
print(dan)

#formatirani ispis pomocu strftime
print(danas.strftime('%a'))
print(danas.strftime('%y'))
print(danas.strftime('%d.%m.%y'))

locale.setlocale(locale.LC_TIME, 'hr_HR') # prebacivanje na hrv jezik i mjesece

print(danas.strftime('%A'))
print(danas.strftime('%y'))
print(danas.strftime('%d.%B.%y'))
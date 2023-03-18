import datetime as dt
import locale

danas = dt.date.today()     # današni datum u obliku YYYY-MM-DD

print(danas)

sada = dt.datetime.now()    # sadašnji trenutak u sekundu
print(sada)

sada_vrijeme = dt.time(12,30,5)     #unos vremena, ne može samo povući podatke
print(sada_vrijeme)

dan = dt.date.weekday(danas)    # Vraća broj od 0-6. ponedjeljak je = 0, utorak = 1 itd...
print(f'Danas je', dan)      

print(danas.strftime('%A'))
print(danas.strftime('%d.%m.%Y'))
print(danas.strftime('%d.%m.%y'))
print(danas.strftime('%dth %B %Y'))

locale.setlocale(locale.LC_TIME, 'hr_HR')

print(danas.strftime('%A'))
print(danas.strftime('%d %B %Y'))

print('\nNjemački jezik')
locale.setlocale(locale.LC_TIME, 'de_DE')

print(danas.strftime('%A'))
print(danas.strftime('%d %B %Y'))

print() #Praazn red
print('Sadašnji trenutak: ',sada.strftime('%d.%m.%Y %H:%M:%S'))

print() #Praazn red
datum = dt.date(2007, 1 ,16)
print(datum)
print(datum.strftime('%d.%m.%Y'))
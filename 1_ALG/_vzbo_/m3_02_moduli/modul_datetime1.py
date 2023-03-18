import datetime as dt
import locale 

danas = dt.date.today() # današnji datum u obliku YYYY-MM-DD

print(danas)

sada = dt.datetime.now()  # sadašnji trenutak

print(sada)

sada_vrijeme = dt.time(12,30,0) # vrijeme kreirano preko parametara koje prenosimo 

print(sada_vrijeme)

a = dt.time(12,30,30,444445)
print(a)

dan = dt.date.weekday(danas) # vraća broj 0-6, počinje 0:ponedjeljak, 1:utorak...
print('Danas je', dan)

# formatirani ispis datume pomoću strftime - koristi objekt date
print(danas.strftime('%A'))
print(danas.strftime('%d.%m.%Y'))
print(danas.strftime('%d.%m.%y'))
print(danas.strftime('%dth %B %Y'))
print('\nHrvatski jezik:')
locale.setlocale(locale.LC_TIME, 'hr_HR')
print(danas.strftime('%A'))
print(danas.strftime('%d. %B %Y'))

print('\nNjemački jezik:')
locale.setlocale(locale.LC_TIME, 'de_DE')

print(danas.strftime('%A'))
print(danas.strftime('%d. %B %Y'))

print('Sadašnji trenutak:', sada.strftime('%d.%m.%Y  %H:%M:%S'))

datum = dt.date(2007, 1, 16)
print(datum)
print(datum.strftime('%d.%m.%Y'))
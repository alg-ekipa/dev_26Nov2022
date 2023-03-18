import datetime as dt
import locale

danas = dt.date.today() #današnji datum u obliku YYYY-MM--DD
print (danas)

sada = dt.datetime.now() #sadašnji trenutak
print (sada)

sada_vrijeme = dt.time (12, 30, 11,555111) #vrijeme kreirano preko parametara koje prenosimo
print (sada_vrijeme)

dan = dt.datetime.weekday (danas) #vraća broj 0-6, počinje 0:ponedjeljak
print ('Danas je', dan)

#formatirani ispis datuma pomoću strftime - koristi objekt date
print (danas.strftime ('%A'))
print (danas.strftime ('%d.%m.%Y.'))
print (danas.strftime ('%d.%m.%y.'))
print (danas.strftime ('%dth %B %Y'))

locale.setlocale(locale.LC_TIME, 'hr_HR')
print
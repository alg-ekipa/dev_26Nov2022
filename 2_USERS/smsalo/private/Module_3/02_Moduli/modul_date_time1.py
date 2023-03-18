import datetime as dt
import locale

danas=dt.date.today()  #današnji datum u obliku yyyy--mm-dd

print(danas)

sada=dt.datetime.now() #sadašnji trenutak
print(sada)

sada_vrijeme= dt.time(12,30,0,201)  #vrijeme kreirano preko parametra koje prenosimo
print(sada_vrijeme)

dan=dt.date.weekday(danas)
print('Danas je', dan)      #vraća broj od 0 do 6, 0=ponedjeljak

if dan ==0:
    print('Dan je ponedjeljak')
else:
    print('Danas nije ponedjeljak')

print(danas.strftime('%A'))
print(danas.strftime('%d.%m.%Y'))       # ispis datuma kao kod nas 18.03.2023       malo m za mjesec, M je za minute
print(danas.strftime('%d.%m.%y'))       # 18.03.23
print(danas.strftime('%dth %B %Y'))    # 18th March 2023

locale.setlocale(locale.LC_TIME, 'hr_HR')       #prebacivanje na hrvatski
print(danas.strftime('%A'))                     #subota
print(danas.strftime('%d.%m.%Y'))       # 18.03.2023
print(danas.strftime('%d.%m.%y'))       # 18.03.23
print(danas.strftime('%d %B %Y'))    # 18 ožujak 2023

locale.setlocale(locale.LC_TIME, 'de_DE')       #prebacivanje na njemački
print(danas.strftime('%A'))                     #Samstang
print(danas.strftime('%d.%m.%Y'))       # 18.03.2023
print(danas.strftime('%d.%m.%y'))       # 18.03.23
print(danas.strftime('%d %B %Y'))    # 18 Marz 2023

print('Sadašnji trenutak ', sada.strftime('%d.%m.%Y %H:%M:%S'))

datum=dt.date(2007,1,16)
print(danas)                            #   2007-01-16
print(datum.strftime('%d.%m.%Y'))       #   16.01.2007

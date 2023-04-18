import datetime as dt
import locale              # idemo prebaciti na lokalne nazive tj. na hrvatski 

danas = dt.date.today()    # hijerarhijski pristup za dohvaćanje današnjeg datuma - yyyy-mm-dd 

print(danas)

# ako želim pogledati malo bolji prikaz za datetime dokumentacije https://docs.python.org/3/library/datetime.html
# ili desi klik na datetime, go to declaration

sada = dt.datetime.now() #sadašnji trenutak u mikrosekundu, ima ga samo datetime

# dt ime datoteke ili modula, datetime ime klase i now

print(sada)

sada_vrijeme = dt.time(12, 30, 0) # proslijedimo mu parametre sat, minuta sekunda koje nam on vrati onda u obliku sat:minuta:sekunda

print(sada_vrijeme)

a = dt.time(12, 30, 30, 666)
print(a)

dan = dt.date.weekday(danas) # vraća broj 0-6, počinje 0:ponedjeljak, 1:utorak... 
print('Danas je', dan)

print(danas.strftime('%A')) # koji je danas dan, vraća naziv daa na engleskom 
print(danas.strftime('%d.%m.%Y'))
print(danas.strftime('%d.%m.%y'))
print(danas.strftime('%dth %B %Y')) # formatirani ispisi datuma pomoću strftime - koristi objekt date (u gore navedenoj adresi na webu ima tablica)

locale.setlocale(locale.LC_TIME, 'hr_HR') # lc_time je varijabla

print('\nHrvatski jezik: ')

print(danas.strftime('%A'))               # dan na hrvatskom
print(danas.strftime('%d. %B %Y'))        # datum u hrvatskom obliku 
print()

locale.setlocale(locale.LC_TIME, 'der_DE')

print('\nNjemački jezik: ')
print(danas.strftime('%A'))               # dan na njemačkom
print(danas.strftime('%d. %B %Y'))
print()

print('Sadašnji trenutak', sada.strftime('%d.%m,%Y %H:%M:%S'))
print()

datum = dt.date(2007, 1, 16)              # po difoltu uvik yyyy-mm-dd
print(datum)
print(datum.strftime('%d.%m.%Y'))         # formatirano sa zadanim parametrima
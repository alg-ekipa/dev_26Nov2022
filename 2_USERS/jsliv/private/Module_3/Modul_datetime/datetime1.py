import datetime as dt
import locale

danas = dt.date.today()

print(danas) #danasnji datum u americkom obliku ymd

sada = dt.datetime.now()  #sadasnji trenutak
print(sada)

sada_vrijeme = dt.time(12,30,0)

print(sada_vrijeme)

a = dt.time(12,30,30,444445)
print(a)

dan = dt.date.weekday(danas)
print("Danas je ", dan)

#formatirani ispis datuma pomoću strftime - koristi objekt date
print(danas.strftime("%A"))
print(danas.strftime("%d.%m.%Y"))
print(danas.strftime("%d.%m.%y"))
print(danas.strftime("%d.%b.%y"))
print(danas.strftime("%d.%B.%y"))
print(danas.strftime("%dth %B %Y"))
print()
locale.setlocale(locale.LC_TIME, "hr_HR")
print(danas.strftime("%A"))
print(danas.strftime("%d.%B.%Y"))
print()

locale.setlocale(locale.LC_TIME, "de_DE")
print(danas.strftime("%A"))
print(danas.strftime("%d.%B.%Y"))
print()

print("Sadašnji trenutak ", sada.strftime("%d.%m.%Y %H:%M:%S"))

datum = dt.date(2015,10,15)
print(datum)
print()
print(datum.strftime("%d.%m.%Y"))





# Prepraviti funkcije da imaju ulazni parametar datum kojeg unosi korisnik, format po izboru
# Neka funkcije samo vraćaju vrijednost (Promijeniti ime!!)
# U glavnom programu napraviti formatirani ispis datuma i vremena!

import datetime as dt

sada = dt.datetime.now()

def ispisi_datum(datum):
    datum1 = dt.datetime.strptime(datum, '%d.%m.%Y')
    datum_objekt = datum1.strftime('%d.%m.%Y')
    return datum_objekt

def ispis_vrijeme(vrijeme):
    vrijeme1 = dt.datetime.strptime(vrijeme, '%d.%m.%Y')
    vrijeme_objekt = vrijeme1.strftime('%H:%M')
    return vrijeme_objekt

def ispisi_razliku(arg1, arg2):
    date_user_obj = dt.datetime.strptime(arg2, '%d.%m.%Y')
    razlika = arg1 - date_user_obj
    return razlika

datum = input("Unesi datum u formatu dd.mm.year: ")
#user_date = '21.12.2012'

print(ispisi_datum(datum))
print(ispis_vrijeme(datum))
print(ispisi_razliku(sada, datum))

#STRP - od objekta radimo STRING
#STRF - od STRINGA radimo objekt
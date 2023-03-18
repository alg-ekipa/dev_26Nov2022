# Prepraviti funkcije da imaju ulazni parametar datum kojeg unosi korisnik, format po izboru
# Neka funkcije samo vraćaju vrijednost (Promijeniti ime!!)
# U glavnom programu napraviti formatirani ispis datuma i vremena!

import datetime as dt

sada=dt.datetime.now()

def ispisi_samo_datum(datum):
    datum_korisnik_obj = dt.datetime.strptime(datum, '%d.%m.%Y.')
    d=datum_korisnik_obj.strftime('%d.%m.%Y')
    return d

def ispisi_samo_datum(vrijeme):
    datum_korisnik_obj = dt.datetime.strptime(vrijeme,'%H:%M:%S')
    t=datum_korisnik_obj.strftime('%H:%M:%S')
    return t

# dopuniti
'''
d = date_user_obj.strftime('%d.%m.%Y')
    return d

def display_time(time):
    date_user_obj = dt.datetime.strptime(time, '%d.%m.%Y')
    #date_user_obj.strftime('%d.%m.%Y %H%M%S')
    return date_user_obj.time()

def display_time_diff(arg1, arg2):
    date_user_obj = dt.datetime.strptime(arg2, '%d.%m.%Y')
    diff = arg1 - date_user_obj
    return diff

user_date = input("Please input the date in fromat dd.mm.year: ")
#user_date = '21.12.2012'

print(display_date(user_date))
print(display_time(user_date))
print(display_time_diff(time_now, user_date))

'''
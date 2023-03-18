# Prepraviti funkcije da imaju ulazni parametar datum kojeg unosi korisnik, format po izboru
# Neka funkcije samo vraćaju vrijednost (Promijeniti ime!!)
# U glavnom programu napraviti formatirani ispis datuma i vremena!

import datetime as dt

sada=dt.datetime.now()

def ispisi_samo_datum(datum):
    datum_korisnik1_obj = dt.datetime.strptime(datum, '%d.%m.%Y.')
    return datum_korisnik1_obj


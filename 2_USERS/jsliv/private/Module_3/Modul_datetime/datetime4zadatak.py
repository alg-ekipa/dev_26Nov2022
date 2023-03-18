# Prepraviti funkcije da imaju ulazni parametar datum kojeg unosi korisnik, format po izboru
# neka funkcije samo vraćaju vrijednost (Promijeniti ime!)
# u glavnom programu napraviti formatirani ispis datuma i vremena!

import datetime as dt

datum_rodjenja = input('Unesite datum rođenja formata dd.mm.yyyy:\n')
datum_rodjenja_obj = dt.datetime.strptime(datum_rodjenja,'%d.%m.%Y')
print(datum_rodjenja_obj.date())
print(datum_rodjenja_obj.year)

datum_sada = input('Unesite današnji datum: dd.mm.yyyy:\n')
datum_sada_obj = dt.datetime.strptime(datum_sada, "%d.%m.%Y")
print(datum_sada_obj.date())
print(datum_sada_obj.year)

def ispis_datum_rodjenja():
    print('Datum rođenja: ', datum_rodjenja_obj.strftime('%d.%m.%Y.'))

def ispis_datum_sada():
    print('Današnji datum: ', datum_sada_obj.strftime('%d.%m.%Y'))

def razlika():
    print('Razlika tog datuma i sadašnjeg je ', datum_sada - datum_rodjenja)
    
ispis_datum_rodjenja()
ispis_datum_sada()
razlika()

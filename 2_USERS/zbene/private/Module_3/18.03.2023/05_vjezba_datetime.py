#Prepraviti funkcije da imaju ulazni parametar datum kojeg unosi korisnik, format po izboru
#neka funkcije samo vraćaju vrijednost (Promijeniti ime!)
#u glavnom programu napraviti formatirani ispis datuma i vremena!

import datetime as dt

datum = input = ('Unesi datum formata dd.mm.yyyyy.: ')
sada = dt.datetime.now()

def ispisi_samo_datum(datum_1):
    datum_2 = dt.datetime.strftime(datum_1, '%d.%m.%Y.') 
    return datum_2
    
def ispisi_samo_vrijeme(vrijeme_2):
    vrijeme_3 = dt.datetime.strftime(vrijeme_2, '%H:%M:%S')
    return vrijeme_3
    
def ispisi_koliko_od_sada(razlika):
    sada3 = dt.datetime.strptime(razlika, 'd.%m.%Y') 
    razlika = sada3 - datum3
    return razlika
    
print(ispisi_samo_datum(datum))
print(ispisi_samo_vrijeme(datum))
print(ispisi_koliko_od_sada(sada, datum))


###ISPRAVI
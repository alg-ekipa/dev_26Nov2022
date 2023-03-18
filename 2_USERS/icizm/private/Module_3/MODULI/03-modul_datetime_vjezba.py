# Prepraviti funkcije da imaju ulazni parametar datum kojeg unosi korisnik, format po izboru
# Neka funkcije samo vraćaju vrijednost (Promjeniti ime!)
# U gavnom programu napraviti formatirani ispis datuma i vremena 


import datetime as dt 


sada = dt.datetime.now()

def izdvoji_samo_datum():
    datum = datum_korisnik_obj.strftime('%d %b %y')
    return datum

def izdvoji_samo_vrijeme(): 
    vrijeme = datum_korisnik_obj.strftime('%H:%M:%S')
    return vrijeme 

def izracunaj_koliko_od_sada():
    razlika = sada - datum_korisnik_obj
    return razlika

datum_korisnik = input('Unesite datum formata dd.mm.yyyy:\n')
datum_korisnik_obj = dt.datetime.strptime(datum_korisnik, '%d.%m.%Y') 
print(datum_korisnik_obj.date())



izdvoji_samo_datum()
izdvoji_samo_vrijeme()
izracunaj_koliko_od_sada()
print(f'Unijeli ste datum {datum}, vrijeme {vrijeme}, od tog datuma do sada je prošlo {razlika}')
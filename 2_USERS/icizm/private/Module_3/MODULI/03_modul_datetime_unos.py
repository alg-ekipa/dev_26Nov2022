import datetime as dt

# kreiranje objekata datetime (datum+vrijeme) preko ulaznih parametara
datum = dt.datetime(2000, 11, 25, 12, 0 , 0)
sada = dt.datetime.now()

print(datum.strftime('%d.%m.%Y.'))                   # formatirani prikaz zadanog datuma

datum_objekt =dt.datetime.strptime('20.4.2021', '%d.%m.%Y')    # ulazni string želimo pretvoriti u objekt datum tako da mu točno kažemu u drugom argumentu gdje se što nalazi
print(datum_objekt)

'''datum_korisnik = input('Unesite datum formata dd.mm.yyyy:\n')
datum_korisnik_obj = dt.datetime.strptime(datum_korisnik, '%d.%m.%Y') #za strptime smo dali dva argumenta, prvi je input korisnika a drugi objašnjava poziciju podataka
print(datum_korisnik_obj.date())
print(datum_korisnik_obj.year)
print()'''

# kreiranje objekata datetime unosom od korinsnika (korisnik unosi string)
datum_korisnik1 = input('Unesite datum formata ime mjeseca (eng.) dd yyyy \n')
datum_korisnik_obj1 = dt.datetime.strptime(datum_korisnik1, '%b %d %Y') 
print(datum_korisnik_obj1.date())


# TO DO: 
# Funcije za ispis samo datuma, ispis samo vremena, koliko ima od sadašnjeg trenutka do datuma koji je unio korisnik 

def ispisi_samo_datum():
    print('Ispis samo datuma: ', datum_korisnik_obj1.strftime('%d.%m.%Y.'))

def ispisi_samo_vrijeme(): 
    print('Ispis samo vrijeme: ', datum_korisnik_obj1.strftime('%H:%M:%S'))

def ispisi_koliko_od_sada():
    print('Razlika od tog datuma do sadašnjeg je:', sada - datum_korisnik_obj1 )

ispisi_samo_datum()
ispisi_samo_vrijeme()
ispisi_koliko_od_sada()


# Prepraviti funkcije da imaju ulazni parametar datum kojeg unosi korisnik, format po izboru
# Neka funkcije samo vraćaju vrijednost (Promjeniti ime!)
# U gavnom programu napraviti formatirani ispis datuma i vremena 
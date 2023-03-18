import datetime as dt

# Kreiranje objekta datetime (datum+vrijeme) preko ulaznih parametara
datum =dt.datetime(2000, 11, 25, 12, 0, 0)
sada = dt.datetime.now()

print (datum.strftime('%d.%m.%Y'))

# Kreiranje objekata preko ulaznog stringa odgovarajućeg oblika
datum_objekt = dt.datetime.strptime('20.4.2021', '%d.%m.%Y')
print(datum_objekt)
'''
datum_korisnik = input('Unesite datum (format DD.MM.YYYY): ')
datum_korisnik_obj = dt.datetime.strptime(datum_korisnik, '%d.%m.%Y')
print(datum_korisnik_obj.date())
print(datum_korisnik_obj.year)
'''
# Kreiranje objekta dateteime unosom od korisnika (korisnik unosi string)
datum_korisnik1 = input('Unesite datum formata (ime mjesec(ENG), dd, yyyy): ')
datum_korisnik_obj1 = dt.datetime.strptime(datum_korisnik1, '%b %d %Y')
print(datum_korisnik_obj1.date())

# Zadatak:
# Funkcije za ispis samo datuma, ispis samo vremena, koliko ima od sadašnjeg trenutka do datuma koji je unio korisnik

def ispisi_samo_datum():
    print('Ispis samo datuma: ',datum_korisnik_obj1.strftime('%d.%m.%Y.'))

def ispisi_samo_vrijeme():
    print('Ispis samo vrijeme: ',datum_korisnik_obj1.strftime('%H:%M:%S'))

def koliko_od_sada():
    print('Razlika tog datuma i sadašnjeg je: ', sada - datum_korisnik_obj1)

ispisi_samo_datum()
ispisi_samo_vrijeme()
koliko_od_sada()


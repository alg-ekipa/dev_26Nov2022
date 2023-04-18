import datetime as dt

#kreiranje objekta datetime(datum+vrijeme) preko laznih parametara
datum=dt.datetime(2000,11,25, 12,0,0)

print(datum.strftime('%d.%m.%Y.'))

#kreiranje objekta datetima preko ulaznog stringa odgovarajućeg oblika
datum_objekt=dt.datetime.strptime('20.4.2021','%d.%m.%Y')
print(datum_objekt)
'''
datum_korisnik=input('Unesite datun formata dd.mm.yyyy: \n')
datum_korisnik_obj=dt.datetime.strptime(datum_korisnik,'%d.%m.%Y')
print(datum_korisnik_obj.date())
print(datum_korisnik_obj.year)
'''
#kreiranje objekta datetime unosom od korisnika(korisnik unosi string)
datum_korisnik1=input('Unesite datun formata ime mjesec (eng.) dd yyyy: \n')
datum_korisnik_obj1=dt.datetime.strptime(datum_korisnik1,'%b %d %Y')
print(datum_korisnik_obj1.date())
sada=dt.time.now

#TO DO:
#Funkcija za ispis samo datuma, ispis samo vremena, koliko ima od sadašnjeg trenutka do datuma koji je unio korisnik

def ispisi_samo_datum():
    print('Ispis samo datuma: ', datum_korisnik_obj1.strftime('%d.%m.%Y.'))

def ispisi_samo_vrijeme():
    print('Ispis samo vrijeme: ', datum_korisnik_obj1.strftime('%H:%M:%S'))

def Koliko_od_sada():
    print('Razlika tog datuma i sadašnjeg je ', sada - datum_korisnik_obj1)

ispisi_samo_datum()
ispisi_samo_vrijeme()
Koliko_od_sada()

#Prepraviti funkcije da imaju ulazni parametar datum kojeg unosi korisnik, format po izboru
#neka funkcije samo vraćaju vrijednost(Promijeniti ime!)
#u glavnom programu napraviti formatirani ispis datuma i vremena!


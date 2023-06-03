import datetime as dt
#kreiranje objekta datetime (datum + vrijeme) preko ulaznih parametara
datum = dt.datetime(2000, 11, 25, 12, 0, 0)
sada = dt.datetime.now()
print (datum.strftime('%d.%m.%Y.'))

datum_objekt = dt.datetime.strptime ('20.04.2021.', '%d.%m.%Y.')
print (datum_objekt)

#kreiranje objekta datetime preko ulaznog stringa odgovarajućeg oblika
'''datum_korisnik = input ('Unesite datum formata dd.mm.yyyy.: ')
datum_korisnik_objekt = dt.datetime.strptime(datum_korisnik, '%d.%m.%Y.')
print (datum_korisnik_objekt.date())
print (datum_korisnik_objekt.year)'''

#kreiranje objekta datetime unosom od korisnika (krisnik unosi string)
datum_korisnik1 = input ('Unesite datum formata ime mjesec (engl.) dd yyyy:\n')
datum_korisnik_objekt1 = dt.datetime.strptime(datum_korisnik1, '%b %d %Y')
print (datum_korisnik_objekt1.date())

#TO DO:
#Funkcije za ispis samo datum, ispis samo vremena, koliko ima od sadašnjeg trenutka koji je unio korisnik

def ispisi_samo_datum():
    print ('Ispis samo datuma: ', datum_korisnik_objekt1.strftime ('%d.%m.%Y.'))

def ispisi_samo_vrijeme():
    print ('Ispis samo vrijeme: ', datum_korisnik_objekt1.strftime ('%H:%M:%S'))

def ispisi_koliko_od_sada():
    print ('Razlika tog datuma i sadašnjeg je', sada - datum_korisnik_objekt1)

ispisi_samo_datum()
ispisi_samo_vrijeme()
ispisi_koliko_od_sada()
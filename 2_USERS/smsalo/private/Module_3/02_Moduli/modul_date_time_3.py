import datetime as dt

sada=dt.datetime.now()
print(sada)

#kreiranje objekta datetime preko ulaznih parametara
datum = dt.datetime(2000, 11, 25, 12, 00, 00)
print(datum.strftime('%d.%m.%Y.'))

datum_objekt=dt.datetime.strptime('20.4.2021', '%d.%m.%Y')
print(datum_objekt)

datum_korisnik= input('Unesite datum formata dd.mm.yyyy: ')
datum_korisnik_obj=dt.datetime.strptime(datum_korisnik, '%d.%m.%Y')     #OD UNESENOG STRINGA ZA DATUM NAPRAVI DATUM OBJEKT KOJI MOŽEMO DALJE KORISTITI 
print(datum_korisnik_obj.date())
print(datum_korisnik_obj.year)
print(datum_korisnik_obj.month)

datum_korisnik1=input('Unesite datum formata: ime mjeseca (eng) dd yyyy: ')
datum_korisnik1_obj=dt.datetime.strptime(datum_korisnik1, '%B %d %Y')
print(datum_korisnik1_obj.date())
                                         
                                         
#to do:
# funkcija za ispis samo datuma, ispis samo vremena, koliko ima od sadašnjeg trenutka do datuma koji je unio korisnik

def ispisi_samo_datum():
    print('Ispis samo datuma: ', datum_korisnik1_obj.strftime('%d.%m.%Y.'))

def ispisi_samo_vrijeme():
    print('Ispis samo vrijeme: ', datum_korisnik1_obj.strftime('%H:%M:%S'))

def koliko_do_sada():
    print('Razlika od tog datuma: ', sada-datum_korisnik1_obj)

ispisi_samo_datum()
ispisi_samo_vrijeme()
koliko_do_sada()


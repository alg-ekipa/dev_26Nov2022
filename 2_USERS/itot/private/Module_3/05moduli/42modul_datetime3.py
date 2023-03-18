import datetime as dt
from dateutil.relativedelta import relativedelta, FR
from dateutil import tz

'''fali'''

datum_korisnik1= input('Unesite datum fomata ime_mjesec(eng) dd yyy:\n')
datum_korisnik_objl = dt.datetime.strptime(datum_korisnik1.'%b %d %y')
print(datum_korisnik_objl.data())

#TO DO
# fukcije za uspis samo datuma, ispis samo vremena, koliko ima od sadasn eg trenutka do datuma koji je unio korisnik


def ispisi_samo_datum():
    print ('Ispis samo datuma: ', datum_korisnik_objl.strftime('%b %d %y'))


# prepraviti funkcije da imaju zlazni patametar datuma kojeg unis korisnik, fomrat po izboru
# neka funkcije samo vracaju vrijednsot (Primjeniti ime!)
# u glavnom programu napraviti fformatiranje ispis datuma i vrenema
import datetime as dt
from dateutil.relativedelta import relativedelta

from dateutil import tz

sadasnji_trenutak=dt.datetime.now()
neki_datum = dt.datetime(2020,10,5,12,0,0)

print ("sadasnji_trenutak", sadasnji_trenutak)
print ('Neki datum:', neki_datum)

print ('Razlika između ta dva datuma/trenutka:', sadasnji_trenutak - neki_datum)


tz_zg = tz.gettz ('Europe/Zagreb')


def ispisi_samo_datum():
    print('Ispisi samo datum ', datum_korisnik_obj1.strftime('%d.%m.%Y.'))


def ispisi_samo_vrijeme():
    print('Ispisi samo datum ', datum_korisnik_obj1.strftime('%d.%m.%Y.'))



def koliko_od_sada():
    print('Ispisi samo datum ', datum_korisnik_obj1.strftime('%d.%m.%Y.'))


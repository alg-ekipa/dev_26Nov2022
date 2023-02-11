import datetime as dt

#generiraj racun
def generiranje_racuna(broj_racuna):
    sadasnji_trenutak = dt.datetime.now()

    sat = sadasnji_trenutak.hour
    minuta = sadasnji_trenutak.minute
    dan = sadasnji_trenutak.day
    mjesec = sadasnji_trenutak.month
    godine = sadasnji_trenutak.year

    racun_id = f'Racun br. {broj_racuna} \tVrijeme izdavanja {sat} : {minuta} {dan}.{mjesec}.{godine}.'
    return racun_id


broj_racuna=1
print (generiranje_racuna(broj_racuna))


import datetime as dt

print(dt.datetime.now())
sat = dt.datetime.now().hour
minuta = dt.datetime.now().minute

godine = dt.datetime.now().year

print(f'sada je {sat} sati, {minuta} minuta u {godine}. godini')

def pozdrav(ime):
    if sat < 11:
        return f'Dobro jutro, {ime}'
    elif 11 <= sat <= 18:
        return f'dobar dan, {ime}'
    else:
        return f'dobro vecer, {ime}'

vase_ime = input ('uneseite svoje ime: ')
print(pozdrav (vase_ime))
        

dan = dt.datetime.now().day
mjesec = dt.datetime.now().month

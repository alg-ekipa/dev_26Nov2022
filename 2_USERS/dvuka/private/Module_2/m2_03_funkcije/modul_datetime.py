import datetime as dt 

print(dt.datetime.now())
sat = dt.datetime.now().hour
minuta = dt.datetime.now().minute

godina = dt.datetime.now().year

print(f'Sada je {sat} sat i {minuta} minuta.')

def pozdrav(ime):
    if sat < 11:
        return f'Dobro jutro, {ime}!'
    elif 11 <= sat < 18:
        return f'Dobar dan, {ime}!'
    else:
        return f'Dobra večer, {ime}!'

vase_ime = input('Unesite svoje ime: ')
pozdrav(vase_ime)


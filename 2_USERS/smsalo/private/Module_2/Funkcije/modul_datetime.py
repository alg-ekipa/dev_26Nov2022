import datetime as dt

print(dt.datetime.now())
sat=dt.datetime.now().hour
minuta=dt.datetime.now().minute

godina=dt.datetime.now().year

print(f'Sada je {sat} sata i {minuta} minuta.')
print()

def pozdrav(ime):           #bez returna uz poziv funkcije
    if sat<11:
        print(f'Dobro jutro, {ime}!')
    elif 11<= sat < 18:
        print(f'Dobar dan, {ime}!')
    else:
        print(f'Dobra večer, {ime}!')

vase_ime=input('Unesite svoje ime: ')
pozdrav(vase_ime)
print()


def pozdrav(ime):               #return i print zajedno
    if sat<11:
        return (f'Dobro jutro, {ime}!')
    elif 11<= sat < 18:
        return (f'Dobar dan, {ime}!')
    else:
        return (f'Dobra večer, {ime}!')

vase_ime=input('Unesite svoje ime: ')
print(pozdrav(vase_ime))

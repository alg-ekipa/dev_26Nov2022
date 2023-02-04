import datetime as dt


sat=dt.datetime.now().hour
minuta=dt.datetime.now().minute
year=dt.datetime.now().year

print( f'{dt.datetime.now()}')

print (f'{sat}:{minuta}')


def pozdrav(ime):
    if sat < 11:
        print(f'Dobro jutro {ime}')

    elif 11<= sat <=18:
         print(f'Dobar dan {ime}')

    else:
         print(f'Dobra večer {ime}')


vase_ime=input ('Unesi svoje ime ')

pozdrav (vase_ime)
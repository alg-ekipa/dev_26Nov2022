import datetime  as dt

print(dt.datetime.now())

sat = dt.datetime.now().hour
print(sat)

def pozdrav(ime):
    if sat<10:
        print(f'Dobro jutro {ime}')     # pošto ovdje imamo "PRINT" kasnije kada pozivamo funkciju ne moramo stavljati print
    elif 10<= sat <= 19:                # kada bi umjesto PRINT bio RETURN onda bi kasnije morali staviti print
        print(f'Dobar dan {ime}')
    else:
        print(f'Dobra večer {ime}')

pozdrav('Hrvoje')


def pozdrav(ime):
    if sat < 11:
        return f'Dobro jutro {ime}!'  
    elif 11 <= sat <= 18:
        return f'Dobar dan {ime}!'
    else:
        return f'Dobra večer {ime}!'

vase_ime = input ('Unesite svoje ime: ')
print(pozdrav(vase_ime))
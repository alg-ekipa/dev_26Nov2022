import datetime as dt

print(dt.datetime.now()) #pokazuje današnji datum i sat (američki) sekunde u decimalama

sat = dt.datetime.now().hour
minuta = dt.datetime.now().minute
godina = dt.datetime.now().year

print(f'Sada je {sat} sati i {minuta} minuta.')

def pozdrav(ime): 
    if sat < 11: 
        print(f'Dobro jutro {ime}!')
    elif 11<= sat < 18: 
        print(f'Dobar dan {ime}!')
    else: 
        print(f'Dobro večer {ime}!')

vase_ime = input('Unesite vaše ime: ')

pozdrav(vase_ime)

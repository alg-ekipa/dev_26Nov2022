#Napravi igru u kojoj treba pogoditi zamišljeni broj

import random
zamisljeni_broj = random.randint(1,51)

while True:
    broj = input('Unesi broj između 1-50: ')

    while broj.isdigit() == False:
        print('Krivi unos! Treba unijet broj u rasponu 1-50')
        broj = input('Unesi broj između 1-50: ')
    
    if 1 <= int(broj) <= 50:
        if int(broj) == zamisljeni_broj:
            print('Pogodak!')
            break
        elif int(broj) < zamisljeni_broj:
            print('Zamisljeni broj je veći od unešenog')
        elif int(broj) > zamisljeni_broj:
            print('Zamisljeni broj je manji od unešenog')
    else:
        print('Broj nije iz zadanog raspona')
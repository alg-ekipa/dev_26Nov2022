# IGRA POGODI BROJ
'''
import random

zamisljeni_broj=random.randint(1,100)
#print(zamisljeni_broj)

while True:
    broj = int(input('Unesi broj: '))
    if broj==zamisljeni_broj:
        print('Točno!')
        break
    elif broj==0:
        break
    elif broj>zamisljeni_broj:
        print('Broj je veći od zadanog')
    elif broj<zamisljeni_broj:
        print('Broj je manji od zadanog')
'''


# TO DO:
# - UNOS STRINGA
# - RASPON BROJEVA
# - NOVA IGRA

import random
zamisljeni_broj=random.randint(1,100)
print(zamisljeni_broj)


igra=1
br_pokusaja=0

while igra:
    broj=input('Unesi broj između 1-100: ')
    isdigit=broj.isdigit()
    if isdigit==True:
        if int(broj)>zamisljeni_broj:
            br_pokusaja+=1
            print('Broj je manji od unešenog')
        elif int(broj)<zamisljeni_broj:
            br_pokusaja+=1
            print('Broj je veći od zamišljenog')
        elif int(broj)==zamisljeni_broj:
            print('Bravo! Pogodili ste broj!')
            
        while True:
            igra=str(input('Želite li igrati ponovo? Y/N: ')).lower()
            if igra=='y':
                br_pokusaja=0
                break
            elif igra=='n':
                igra=0
                break
            else:
                print('krivi unos ')
    else:
        print('Niste unjeli broj')
        continue

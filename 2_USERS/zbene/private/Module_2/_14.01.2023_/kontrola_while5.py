#IGRA POGODI BROJ
import random

zamisljeni_broj = random.randint(1,100)
odgovor = ('n', 'N', 'd','D')
upit = 'd'

#print(zamisljeni_broj)

while 1:
    broj = input('Unesi broj: ')
    while broj.isdigit() == False:
        print('Krivi unos! Morate unijeti broj! Ponovite unos!')
        broj = input('Unesi broj: ')   
    
    if 0 < int(broj) < 101:
        if int(broj) == zamisljeni_broj:
            print('Pogodili ste broj!')
            zamisljeni_broj =random.randint(1,100)
            upit = input('Želite li igrati novu igru? n - ne; d - da')
            while 1 not in upit:
                
        if int(broj) < zamisljeni_broj:
            print('Uneseni broj je manji od traženog, pokušajte ponovo')
        if int(broj) > zamisljeni_broj:
            print('Uneseni broj je veći od traženog, pokušajte ponovo')
    else:
        print(f'Broj {broj} nije u zadanom rasponu, pokušajte ponovo!')
        broj = input('Unesi broj: ')
    
    
#TO DO:
# - unos stringa
# - raspon brojeva
# - nova igra
# igra pogodi broj 24

'''pogodi = 24

while 1:
    broj = int(input('unesi broj! '))
    if broj > pogodi:
        print('Broj je manji od trazenog!')
    if broj < pogodi:
        print('broj je veci od trazeog!')
    if broj == pogodi:
        break
print('Pogodili ste broj!')
'''

'''import random
pogodi = random.randint(1,100)

while 1:
    broj = input('unesi broj! ')
    while broj.isdigit() == False:
        print('Krivi unos, morate unijeti broj, ponovo unos!')
        broj = input('unesi broj! ')
        if 0 < int(broj) < 101:
            break
        else:
            print('Broj nije u zadanom rasponu, pokušajte ponovo!')
    if int(broj) > pogodi:
        print('Broj je manji od trazenog!')
    if int(broj) < pogodi:
        print('broj je veci od trazeog!')
    if broj == pogodi:
        break
print('Pogodili ste broj!')'''


import random
pogodi = random.randint(1,100)

game='D'
odogovor=('n','N','d','D')
brojac=0


while game.upper() == 'D':
    broj = input('unesi broj! ')
    while broj.isdigit() == False:
        print('Krivi unos, morate unijeti BROJ, ponovo unosi!')
        brojac += 1
        broj = input('unesi broj! ') 

    if 0 < int(broj) < 101:
        brojac += 1
        if int(broj) > pogodi:
            print('Broj je MANJI od trazenog!')
        if int(broj) < pogodi:
            print('broj je VECI od trazeog!')
            
        if int(broj) == pogodi:
            print(f'Pogodili ste broj iz {brojac} pokušaja!')
            pogodi = random.randint(1,100)
            brojac = 0
            game = input('Želite li novu igru? n - ne; d- da')
            while game not in odogovor:
                game = input('Pogrešan unos. Želite li novu igru? n - ne; d- da: ')
            if game.upper() == 'N':
                break
   
    else:
        print('Broj nije u zadanom rasponu, pokušajte ponovo!')
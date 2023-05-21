import random
pogodi = random.randint(1,100)

game='D'
odogovor=('n','N','d','D')



while game.upper() == 'D':
    broj = input('unesi broj! ')
    while broj.isdigit() == False:
        print('Krivi unos, morate unijeti BROJ, ponovo unosi!')
        broj = input('unesi broj! ')

    if 0 < int(broj) < 101:
        if int(broj) > pogodi:
            print('Broj je MANJI od trazenog!')
        if int(broj) < pogodi:
            print('broj je VECI od trazeog!')
        if int(broj) == pogodi:
            print('Pogodili ste broj!')
            pogodi = random.randint(1,100)
            game = input('Želite li novu igru? n - ne; d- da')
            while game not in odogovor:
                game = input('Pogrešan unos. Želite li novu igru? n - ne; d- da: ')
            if game.upper() == 'N':
                break
            
    else:
        print('Broj nije u zadanom rasponu, pokušajte ponovo!')
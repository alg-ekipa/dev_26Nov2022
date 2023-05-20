import random

odabir = ['r', 'p', 's']
PC = random.choice(odabir)

igra = str(input('Želite igrati "Rock paper scissors"? Y,N: ')).lower()
if igra == 'y':
                
    while igra =='y':
        čovjek = input ('Unesi odabir (r, p, s): ')
        if čovjek in odabir:
            print(f'\nOdabrali ste {čovjek} a PC {PC}.\n')
            if čovjek =='r' and PC =='r':
                print('Neriješeno!')
            elif čovjek =='r' and PC =='s':
                print('Pobijedili ste!')
            elif čovjek =='r' and PC =='p':
                print('PC je pobijedio!')
            elif čovjek =='s' and PC =='s':
                print('Neriješeno!')
            elif čovjek =='s' and PC =='r':
                print('PC je pobijedio!')    
            elif čovjek =='s' and PC =='p':
                print('Pobijedili ste!')
            elif čovjek =='p' and PC =='p':
                print('Neriješeno!!')
            elif čovjek =='p' and PC =='r':
                print('Pobijedili ste!')
            elif čovjek =='p' and PC =='s':
                print('PC je pobijedio!')
            while True:
                igra = str(input('Želite li igrati ponovo?) Y/N: ')).lower()
                if igra =='y':
                    break
                elif igra == 'n':
                    igra = 0
                    break
                else:
                    print('Pogrešan unos!')
        else:
            print('Pogrešan unos')
            continue
else:
    print('Pogrešan unos')
    igra = str(input('Želite igrati Rock paper scissors?) Y,N: ')).lower()

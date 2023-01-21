while True:

    print('Odaberi konverziju:  \n 1-udaljenost \n 2-temperatura \n 3-težina \n 4-volumen \n 5-snaga \n')
    konv=int(input('Unesi broj oznake konverzije: '))

    if konv==1:
        smjer=input('Odabrali ste konverziju udaljenosti. Odaberite smjer konverzije: \n a - iz km u milju \n b - iz milje u km \n ')
        if smjer=='a':
            km=float(input('Unesite kilometre: '))
            milja=km*0.6214
            print(f'{km} kilometara iznosi {milja} milja.')
        elif smjer=='b':
            milja=float(input('Unesite milje: '))
            km=milja/0.6214
            print(f'{milja} milja iznosi {km} kilometara.')
    
    if konv==2:
        smjer=input('Odabrali ste konverziju temperature. Odaberite smjer konverzije: \n a - iz °C u °F \n b - °F u °C \n ')
        if smjer=='a':
            temp_C=int(input('Unesite temperaturu u °C: '))
            temp_F=temp_C*(9/5)+32
            print(f'{temp_C} °C iznosi {temp_F} °F.')
        elif smjer=='b':
            temp_F=int(input('Unesite temperaturu u °F: '))
            temp_C=(temp_F-32)/9/5
            print(f'{milja} milja iznosi {km} kilometara.')

    odluka=input('Zelite li nastaviti unositi? Za DA unesite 1, za NE unesite 0. ')
    if odluka=='0':
        break
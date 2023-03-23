import random

ukupno_igri = int(input('Unesi koliko želiš puta igrati: '))
br_igre = 1

igrač_pobjeda = 0
kompjuter_pobjeda = 0

while int(br_igre) <= ukupno_igri:
    kompjuter = random.randint(1,3)
    if  kompjuter == 1:
        kompjuter = 1 #kamen
    elif kompjuter == 2:
        kompjuter = 2 #škare
    else:
        kompjuter = 3 #papir

    print()
    print('Unesite broj za odabir: \n\t1. kamen\n\t2. šakre\n\t3. papir')
    igrač = int(input('Tvoj odabir je: '))



    if igrač == kompjuter:
        print('Neriješeno!!')
        print(f'Rezultat je IGRAČ: {igrač_pobjeda} - KOMPJUTER: {kompjuter_pobjeda}')
    elif igrač == 1 and kompjuter == 2:
        print('Igrač pobjeđuje!!')
        igrač_pobjeda +=1
        print(f'Rezultat je IGRAČ: {igrač_pobjeda} - KOMPJUTER: {kompjuter_pobjeda}')
    elif igrač == 1 and kompjuter == 3:
        print('Kompjuter pobjeđuje!!')
        kompjuter_pobjeda += 1
        print(f'Rezultat je IGRAČ: {igrač_pobjeda} - KOMPJUTER: {kompjuter_pobjeda}')
    elif igrač == 2 and kompjuter == 1:
        print('Kompjuter pobjeđuje!!')
        kompjuter_pobjeda += 1
        print(f'Rezultat je IGRAČ: {igrač_pobjeda} - KOMPJUTER: {kompjuter_pobjeda}')
    elif igrač == 2 and kompjuter == 3:
        print('Igrač pobjeđuje!!')
        igrač_pobjeda +=1
        print(f'Rezultat je IGRAČ: {igrač_pobjeda} - KOMPJUTER: {kompjuter_pobjeda}')
    elif igrač == 3 and kompjuter == 2:
        print('Kompjuter pobjeđuje!!')
        kompjuter_pobjeda += 1
        print(f'Rezultat je IGRAČ: {igrač_pobjeda} - KOMPJUTER: {kompjuter_pobjeda}')
    elif igrač == 3 and kompjuter == 1:
        print('Igrač pobjeđuje!!')
        igrač_pobjeda +=1
        print(f'Rezultat je IGRAČ: {igrač_pobjeda} - KOMPJUTER: {kompjuter_pobjeda}')
    
    br_igre+=1


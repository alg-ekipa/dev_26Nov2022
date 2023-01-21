#IGRA POGODI BROJ


import random #GENERIRAJ RANDOM BROJ
zamisljeni_broj = random.randint(1,100) #GENERIRAJ RANDOM BROJ OD 1-100
#print(zamisljeni_broj)  sakrij prikaz random broja

while 1:
    broj=int(input('Unesi broj: '))
    if broj==zamisljeni_broj:
        print('Pogodili ste zadani broj! ČESTITAMO!!!')
        break
    elif broj==0:
        break
    elif broj > zamisljeni_broj:
        print('Broj je veći od zadanog, pokušajte ponovo!')
    elif broj < zamisljeni_broj:
        print('Broj je manji od zadanog, pokušajte ponovo!')
    

'''
ZADATAK
to do:

*UNOS STRINGA
*RASPON BROJEVA
*NOVA IGRA?
'''
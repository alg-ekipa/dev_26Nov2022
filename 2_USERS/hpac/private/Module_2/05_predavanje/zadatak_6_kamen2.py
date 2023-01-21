# kamen škare papir igra - računalo nasumično bira 

import random

x = int(input('Unesite koliko partija želite igrati: '))

igrac_pobjede = 0
racunalo_pobjede = 0

for i in range(1,x+1):

    kompjuter_odabir = random.randint(1,3)
    if kompjuter_odabir == 1:
        kompjuter_odabir = 1 #kamen
    elif kompjuter_odabir == 2:
        kompjuter_odabir = 2 #škare
    else:
        kompjuter_odabir = 3


    print('Izaberite:\n\t1. kamen\n\t2. škare\n\t3. papir')
    igrač_odabir = int(input('Vaš odabir:  '))
    
    if igrač_odabir == kompjuter_odabir:
        print('Neriješeno!!')
    elif igrač_odabir == 1 and kompjuter_odabir == 2:
        print('Igrač pobjeđuje')
        igrac_pobjede += 1
    elif igrač_odabir == 1 and kompjuter_odabir == 3:
        print('Računalo pobjeđuje')
        racunalo_pobjede += 1
    elif igrač_odabir == 2 and kompjuter_odabir == 1:
        print('Računalo pobjeđuje')
        racunalo_pobjede += 1
    elif igrač_odabir == 2 and kompjuter_odabir == 3:
        print('Igrač pobjeđuje')
        igrac_pobjede += 1
    elif igrač_odabir == 3 and kompjuter_odabir == 2:
        print('Računalo pobjeđuje')
        racunalo_pobjede += 1
    elif igrač_odabir == 3 and kompjuter_odabir == 1:
        print('Igrač pobjeđuje')
        igrac_pobjede += 1
    
    i=i+1
print(f'Igrac ima {igrac_pobjede} pobjedu, a računalo {racunalo_pobjede} pobjeda')
# kamen škare papir igra - računalo nasumično bira 

import random

nastavak = 1

while nastavak == 1:

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
    elif igrač_odabir == 1 and kompjuter_odabir == 3:
        print('Računalo pobjeđuje')
    elif igrač_odabir == 2 and kompjuter_odabir == 1:
        print('Računalo pobjeđuje')
    elif igrač_odabir == 2 and kompjuter_odabir == 3:
        print('Igrač pobjeđuje')
    elif igrač_odabir == 3 and kompjuter_odabir == 2:
        print('Računalo pobjeđuje')
    elif igrač_odabir == 3 and kompjuter_odabir == 1:
        print('Igrač pobjeđuje')
    
    print('Želite li još igrati:\n 1. Da\n 2. Ne')
    nastavak=int(input())
    if nastavak == 1:
        nastavak = 1
    else:
        nastavak = 0
   
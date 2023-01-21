import random

    print('Želiš igrati Rock paper scissors?:' 'Napiši y ako želiš igrati')

odabir = ['r', 'p', 's']
PC = random.choice(odabir)

while odabir == True:
    odabir_racunala = random.randint('r' or 'p' or 's')
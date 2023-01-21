'''Napravite aplikaciju za konverziju (u oba smjera):
• km u milju – (1 km = 0.6214 milje)
• °C u °F – (0°C = 32°F) obrnuto 𝑇(°ி) = 𝑇(°஼) ∗ (9/5) + 32
• kg u funtu (pounds) – 1 kg = 2.2046 pounds
• Litra u US galon – 1l = 0.2642 US gal
• kW (kilowatt) u ks (horsepoweer ili konjska snaga) – 1 kW = 1.3596'''
while True: 
    zadatak = input(f'Dobro došli u program za konverziju mjernih jedinica! \nOdaberite konverziju: \n\t 1) udaljenost \n\t 2) temperatura \n\t 3) težina \n\t 4) volumen \n\t 5) snaga \n ')
    if zadatak == '1':
        udaljenost = input(f'Odaberite konverziju: \n\t a) Iz kilometra u milje \n\t b) Iz milja u kilometre \n')
        if udaljenost == 'a':
            km = int(input('Odabrali ste konverziju iz kilometara u milje. Unesite broj kilometara: '))
            print(f'{km} kilometara iznosi {km*0.6214} milja')
        if udaljenost == 'b':
            milja = int(input('Odabrali ste konverziju iz milja u kilometre. Unesite broj milja: '))
            print(f'{milja} milja iznosi {milja/0.6214} kilometara')
    if zadatak == '2':
        temperatura = input(f'Odaberite konverziju: \n\t a) Iz °C u °F \n\t b) Iz °F u °C \n')
        if temperatura == 'a':
            c = int(input('Odabrali ste konverziju iz °C u °F. Unesite °C: '))
            print(f'{c}°C iznosi {c * 1.8 + 32}°F')
        if temperatura == 'b':
            f = int(input('Odabrali ste konverziju iz °F u °C. Unesite °F: '))
            print(f'{f}°F iznosi {(f - 32) * 0.5556}°C')
    
    #else: 
    #    print('Niste unijeli dobar odabir!') 

    kraj = input('Želite li novu konverziju? Odaberi da ili ne  ')
    if kraj == 'ne':
        break
    
    

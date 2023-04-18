def duljina(dulj):
    print('Odaberite konverziju: a) Iz kilometara u milje\n b) Iz milja u kilometre')
    kontrola = input()

    if kontrola == 'a':
        print('Odabrali ste konverziju iz kilometara u milje. Unesite broj kilometara: ')
        km = float(input())
        milja = km*0.6214
        print(f'{km} km iznosi {milja} milja')
    if kontrola == 'b':
        print('Unesite broj milja: ')
        m = float(input())
        kilom = m/0.6214
        print(f'{m} milja iznosi {kilom} km.')

def temperatura(temp):
    print('Odaberite konverziju:\n a) Iz Celsiusa u Fahrenheite\n b) Iz Fahrenheite u Celsiuse')
    kontTemp = input()

    if kontTemp == 'a':
        print('Odabrali ste konverziju iz Celsiusa u Fahrenheite. Unesite temperaturu: ')
        stupnj_C = float(input())
        stupnj_F = (stupnj_C*(9/5)) + 32
        print(f'{stupnj_C}°C iznosi {stupnj_F}°F')
    if kontTemp == 'b':
        print('Odabrali ste konverziju iz Fahrenheite u Celsiuse. Unesite temperaturu: ')
        stupnj_F2 = float(input())
        stupnj_C2 = (5*(stupnj_F2 -32))/9
        print(f'{stupnj_F2}°F iznosi {stupnj_C2}°C')   

def tezina(tez):
    print('Odaberite konverziju:\n a) Iz kilograma u funtu\n b) Iz funti u kilograme')
    kontTez = input()

    if kontTez == 'a':
        print('Odabrali ste konverziju iz kilograma u funte. Unesite broj kilometara: ')
        kilo1 = float(input())
        funt1 = kilo1*2.2046
        print(f'{kilo1} kg iznosi {funt1} funti')
    if kontTez == 'b':
        print('Odabrali ste konverziju iz funti u kilograme. Unesite broj funti: ')
        funt2 = float(input())
        kilo2 = funt2/2.2046
        print(f'{funt2} funti iznosi {kilo2} kg')

def volumen(volu):
    print('Odaberite konverziju:\n a) Iz litra u galone\n b) Iz galona u litre')
    kontVol = input()

    if kontVol == 'a':
        print('Odabrali ste konverziju iz litra u galone. Unesite broj litara: ')
        lit1 = float(input())
        gal1 = lit1*0.2642
        print(f'{lit1} L iznosit {gal1} US gal')
    if kontVol == 'b':
        print('Odabrali ste konverziju iz galona u litre. Unesite broj galona: ')
        gal2 = float(input())
        lit2 = gal2/0.2642
        print(f'{gal2} uS gal iznosi {lit2} L')

def snaga(snag):
    print('Odaberite konverziju:\n a) Iz kilovata u konjske snage\n b) Iz konjskih snaga u kilovate')
    kontSna = input()

    if kontSna == 'a':
        print('Odaberiali ste konverziju iz kilovata u konjsku snagu. Unesite broj: ' )
        kw1 = float(input())
        ks1 = kw1*1.3596
        print(f'{kw1} kW iznosi {ks1} KS')
    if kontSna == 'b':
        print ('Odaberiali ste konverziju iz konjske snage u kilovate. Unesite broj: ')
        ks_2 = float(input())
        kw_2 = ks_2/1.3596
        print(f'{ks_2} KS iznosi {kw_2} kW')


print('Dobrodošli u program za konverziju mjernih jedinica!')
#print('Odaberite konverziju:\n 1) udaljenost\n 2) temperature\n 3) težina\n 4) volumen\n 5) snaga')

i=1

while (i==1):
    print('Odaberite konverziju:\n 1) udaljenost\n 2) temperature\n 3) težina\n 4) volumen\n 5) snaga')
    x = int(input())
    if x == 1:
        duljina(x)
    if x == 2:
        temperatura(x)
    if x == 3:
        tezina(x)
    if x == 4:
        volumen(x)
    if x == 5:
        snaga(x)
    odabir_ponovno=int(input('Želite li novu konverziju? Odaberi 1 za Da ili 2 za Ne'))
    if odabir_ponovno==1:
        i==1
    elif odabir_ponovno==2:
        i==2
    else:
        print('Neispravan unos!')
        break
    







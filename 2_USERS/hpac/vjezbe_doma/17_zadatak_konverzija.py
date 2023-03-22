# potrebno je napraviti program za konverziju  u oba smjera
# 1km = 0,6214 milje
# 0C = 0F -->  Tf = Tc*9/5 + 32
# 1kg = 2,2046pounds
# 1l = 0,2642 US gal
# 1kW = 1,3596KS

print('Koju konverziju želiš napraviti:\n\t1. Udaljenost\n\t2. Temperatura\n\t3. Masa\n\t4. Volumen\n\t5. Snaga')
odluka = int(input('Unesi broj ispred željene konverzije: '))

while odluka in range(1,5):
    if odluka == 1:
        print('Koju konverziju želite:\n\ta. km u milje\n\tb. milje u km')
        odluka_2 = (input('Unesi broj ispred željene konverzije: '))
        if odluka_2 == 'a':
            print('Unesite broj kilometara: ')
            udaljenost = float(input( ))
            print(f'{udaljenost}km iznosi {round(udaljenost/0.6214,2)}m')
        if odluka_2 == 'b':
            print('Unesite broj milja: ')
            udaljenost = float(input( ))
            print(f'{udaljenost}m iznosi {round(udaljenost/1.61,2)}km')
        else:
            break
    else:
        break
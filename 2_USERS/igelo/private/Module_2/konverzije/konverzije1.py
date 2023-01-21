"""
Napravite apliklaciju za konverziju u oba smjera:
- km u milje (1km = 0.6214 milje)
- C u F - (0c = 32f) ****  T(f) = T(c)*(9/5)+32
- kg u funtu (1kg = 2.2046 funti)
- litra u galon (1l = 0.2642 US gal)
- kW(kilowatt) u ks(kojnske snage ili horsepower) (1kW = 1.3596 ks/hp)
"""

a=('1 = km u milje')
b=('2 = Celziuse u Farenheit')
c=('3 = KG u Punds ')
d=('4 = Litre u galone')
e=('5 = kilowatte u konjsku snagu (KS/HP)')

print('Odaberite željenu konverziju:')
print(a)
print(b)
print(c)
print(d)
print(e)
print()

f=int(input('Unesite izor sa brojem od 1 do 5:'))
if f ==1:
    print('Odabrali ste konverziju km-a u milje.')
    a1=float(input('Unesite kilometre:'))*0.6214
    print(f'{a1} milja/e.')
if f ==2:
    print('Odabrali ste konverziju Celziusa u Farenheit.')
    b1=float(input('Unesite Celziuse:'))*(9/5)+32
    print(f'{b1} Farenheita.')
if f ==3:
    print('Odabrali ste konverziju kilograma u pounds.')
    c1=float(input('Unesite kilograme:'))*2.2046
    print(f'{c1} pounds.')
if f ==4:
    print('Odabrali ste konverziju litre u galon.')
    d1=float(input('Unesite litre:'))*0.2642
    print(f'{d1} galon/a.')
if f ==5:
    print('Odabrali ste konverziju kilowatt-a u KS(HP)')
    e1=float(input('Unesite kilowatte:'))*1.3596
    print(f'{e1} KS-a/e.')
if f !=(1,6):
    f=int(input('Pokušajte ponovno N=0 / Y=1'))
    


    





"""
a1=float(input('Unesite kilometre:'))*0.6214
print(f'{a1} miles.')
"""
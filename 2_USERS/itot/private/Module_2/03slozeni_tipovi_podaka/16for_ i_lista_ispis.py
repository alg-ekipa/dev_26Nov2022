# for petalja sa range start 1, stop 11 (-1 od željenog), po 1 korak (broj)

for i in range (0,11,1):
    print(i, end=' ')

print()
    
for i in range (100,0,-5):  # u nazad odbrojavanje
    print(i, end=' ')

print()

#zbroj brojeva od 1 do 20
zbroj=0

for i in range (21): # ako nema Start onda je 0, ako nema step onda je 1
    zbroj += i

print(zbroj) 
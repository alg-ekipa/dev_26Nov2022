#naredba samo IF

a=5

if a<10:
    print(f'Broj {a} je manji od 10')
print("Sada smo izvan if petlje")
print()

#naredba IF ELSE

b=10
if b<15:
    print(f'Broj {b} je manji od 15')
    print('Sada smo u bloku IF')
else:
        print(f'Broj {b} NIJE manji od 15')
        print('Sada smo u bloku ELSE')
print('Sada smo izvan bloka IF ELSE')
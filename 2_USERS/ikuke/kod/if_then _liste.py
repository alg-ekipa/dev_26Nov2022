

brojevi= [31, 22, 43, 41, 30, 51, 52, 22, 11, 31 ]
print(len(brojevi))
broj_brojeva=len(brojevi)

for broj in brojevi: # za svaki broj unutar liste brojevi
    print(broj)





for broj in brojevi:
    if broj%9 == 0:
        print(f'Broj {broj} je djeljiv s 9')
    if broj%6 == 0:
        print(f'Broj {broj} je djeljiv s 6')
    if broj%3 == 0:
        print(f'Broj {broj} je djeljiv s 3')
    else:
        print(f'Broj {broj} nije djeljiv ni s 3 ni s 6 ni s 9')
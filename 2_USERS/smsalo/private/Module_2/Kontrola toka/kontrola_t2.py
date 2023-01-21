# djeljivost s 3

brojevi=[]
for broj in range (1,31):
    brojevi.append(broj)
# print(brojevi)

for broj in brojevi:
    if broj%3==0:
        print(f'Broj {broj} je djeljiv s 3')
        if broj%6==0:
            print(f'Broj {broj} je djeljiv s 6')   
        if broj%9==0:
            print(f'Broj {broj} je djeljiv s 9')
    else:
        print(f'Broj {broj} nije djeljiv ni s 3, ni s 6, ni s 9')
print()


for broj in brojevi:
    if broj%3==0:
        print(f'Broj {broj} je djeljiv s 3')
    if broj%6==0:
            print(f'Broj {broj} je djeljiv s 6')   
    if broj%9==0:
            print(f'Broj {broj} je djeljiv s 9')
    else:
        print(f'Broj {broj} nije djeljiv ni s 3, ni s 6, ni s 9')
print()



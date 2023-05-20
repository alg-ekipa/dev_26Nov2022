# Djeljivost sa 3 (slide 95, 04dio 02 osnove programiranja)

brojevi = []

for broj in range (1,31):
    brojevi.append(broj)

#print(brojevi)

for broj in brojevi:
    if broj%9 == 0:
        print(f'Broj {broj} je djeljiv sa 9')
    if broj%6 == 0:
        print(f'Broj {broj} je djeljiv sa 6')
    if broj%3 == 0:
        print(f'Broj {broj} je djeljiv sa 3')
    else:
        print(f'Broj {broj} nije djeljiv ni sa 3, ni sa 6, ni sa 9')

'''
for broj in brojevi:
    if broj%3 == 0:
        print(f'Broj {broj} je djeljiv sa 3')
        if broj%6 == 0:
            print(f'Broj {broj} je djeljiv sa 6')
        if broj%9 == 0:
            print(f'Broj {broj} je djeljiv sa 9')
    else:
        print(f'Broj {broj} nije djeljiv ni sa 3, ni sa 6, ni sa 9')
'''
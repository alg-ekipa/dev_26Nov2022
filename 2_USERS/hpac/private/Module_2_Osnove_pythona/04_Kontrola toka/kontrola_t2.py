#djeljivost s 3

brojevi = []

for broj in range(1,31):
    brojevi.append(broj)

#print(brojevi)  - DODANO SAMO RADI KONTROLE (da li je uneseno u listu)
'''
for broj in brojevi:
    if broj%9 == 0:
        print(f'Broj {broj} je dijeljiv sa 9')
    if broj%6 == 0:
        print(f'Broj {broj} je dijeljiv sa 6')
    if broj%3 == 0:
        print(f'Broj {broj} je dijeljiv sa 3')
    else:
        print(f'Broj {broj} NIJE djeljiv ni sa 3, ni  6 , ni 9')
'''

'''
for broj in brojevi:
    if broj%9 == 0:
        print(f'Broj {broj} je dijeljiv sa 9')
        if broj%6 == 0:
            print(f'Broj {broj} je dijeljiv sa 6')
        if broj%3 == 0:
            print(f'Broj {broj} je dijeljiv sa 3')
    else:
        print(f'Broj {broj} NIJE djeljiv ni sa 3, ni  6 , ni 9')
'''



for broj in brojevi:
    if broj%3 == 0:
        print(f'Broj {broj} je dijeljiv sa 3')
        if broj%6 == 0:
         print(f'Broj {broj} je dijeljiv sa 6')
        if broj%9 == 0:
         print(f'Broj {broj} je dijeljiv sa 9')
    else:
        print(f'Broj {broj} NIJE djeljiv ni sa 3, ni  6 , ni 9')
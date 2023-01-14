# djeljivost sa 3

brojevi = []

for broj in range(1,31):
    brojevi.append(broj)

# print(brojevi) provjera liste

for broj in brojevi:
    if broj%9==0:
        print(f'broj {broj} je djeljiv sa 9')
    if broj%6==0:
        print(f'broj {broj} je djeljiv sa 6')
    if broj%3==0:
        print(f'broj {broj} je djeljiv sa 3')
    else:
        print(f'broj {broj} nije djeljiv sa 3, 6 i 9')
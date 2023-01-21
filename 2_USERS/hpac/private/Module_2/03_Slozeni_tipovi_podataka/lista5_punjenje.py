brojevi = []
brojevi1 = []
'''
brojevi.append(3)
brojevi.append(4)
brojevi.append(7)
brojevi.append(1)
brojevi.append(8)
print(brojevi)'''

for broj in range(1,101):
    brojevi.append(broj)

print(brojevi)

for broj1 in range(50,101,5):
    brojevi1.append(broj1)
print(brojevi1)

for broj in brojevi1:
    print(broj, end=' ')

print()  #zamjena vrijednosti elementa
brojevi1[0]=1000
print(brojevi1)

print()
print(f'Broj clanova lista brojevi je {len(brojevi)}')
print(f'Broj clanova lista brojevi1 je {len(brojevi1)}')
'''

brojevi = []

for broj in range (1,101): # dodavanje brojeva uz pomoć range
    brojevi.append(broj)

print(brojevi)
'''

brojevi1 =  []

for i in range (50, 101, 5):
    brojevi1.append(i)

print(brojevi1)

brojevi1[0] = 1000

print(brojevi1)

print(f'Broj čjanova liste brojevi1 je {len(brojevi1)}')
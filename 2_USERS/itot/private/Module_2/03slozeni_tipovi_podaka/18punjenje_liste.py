

brojevi=[]
brojevi_1=[]

for broj in range (1,101):
    brojevi.append(broj)

print (brojevi)


for i in range(50,101,5):
    brojevi_1.append(i)

print(brojevi_1)

print(f'Broj clanova liste Brojevi: {len(brojevi)}')
print(f'Broj clanova liste Brojevi_1: {len(brojevi_1)}')
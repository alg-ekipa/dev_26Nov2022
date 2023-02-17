brojevi = []
brojevi1 = []

for i in range(100):
    brojevi.append(i)
print(brojevi)

print()

for b in range(100,1000,7):
    brojevi1.append(b)
print(brojevi1)

duljina = len(brojevi)  
duljina1 = len(brojevi1)  

print(f'U prvom nizu ima ukupno {duljina} brojeva, a u drugom {duljina1}')
brojevi_1=[]

"""
brojevi.append(2)
brojevi.append(3)
brojevi.append(8)
brojevi.append(112)
brojevi.append(24)
print(brojevi)
"""

for broj_1 in range (1,101):
    brojevi_1.append(broj_1)
print (brojevi_1)

brojevi_2=[]
for broj_2 in range (100,0,-5):
    brojevi_2.append(broj_2)
print(brojevi_2)
for broj_2 in brojevi_2:
    print (broj_2, end=" ")

print()
brojevi_2[0]=1000
print(brojevi_2)

print(f"Broj članova liste brojevi_2 je {len(brojevi_2)}")

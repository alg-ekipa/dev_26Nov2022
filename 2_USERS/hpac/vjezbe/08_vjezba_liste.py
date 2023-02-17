for i in range(10):
    print(i, end=' ')
print()

for i in range(1,10,3):
    print(i, end=' ')

#zadatak: izračunaj prosjek ocjena u razredu

print()

ocjene = [1,2,3,4,5,5,3,2,5,3,4,1,2,5,4,3,3,2]
print(len(ocjene))
suma = 0

for i in ocjene:
    suma =+ suma + i

print(suma)
prosjek = suma/len(ocjene)

print(f'Prosjek ocjena razreda je {round(prosjek,2)}, a u razredu ima {len(ocjene)} učenika')
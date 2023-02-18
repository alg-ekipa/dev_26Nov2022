#Unosimo 5 učenika peko tipkovnice 8IMENA SVAKOM UČENIKU UNOSIMO IME i 3 ocjene ina kraj uispisujemo dobiveni rječnik

ucenici_ocjene={}

for i in range(5):
    kljuc=input(f'Unesi ime {i+1}. učenika: ')
    lista_ocjena=[]
    for j in range(3):
        vrijednost=int(input(f'Unesi {j+1}. ocjenu učenika: '))
        lista_ocjena.append(vrijednost)
        ucenici_ocjene[kljuc]=lista_ocjena

print(ucenici_ocjene)

print('Učenik     Ocjene')
for k,v in ucenici_ocjene.items():
    print(k, ':')
    print(f'{k}    {v}')
    
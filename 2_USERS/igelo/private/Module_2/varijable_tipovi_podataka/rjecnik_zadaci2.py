# Unosimo preko tipkovnice (imena), svakom učeniku
#unosimo po 3 ocijene



ucenici_ocijene=[]

for i in range(5):
    kljuc=input(f'Unesi ime {i+1}. učenika:')
    lista_ocijena=[]
    for j in range(3):
        vrijednost= int(input(f'Unesi {j+1}. ocijenu učenika:'))
        lista_ocijena.append(vrijednost)
        ucenici_ocijene[kljuc] = lista_ocijena

    print(ucenici_ocijene)

print('Učenik    Ocijene')
for k,v in ucenici_ocijene.items():
        print(f'{k} : {v}')
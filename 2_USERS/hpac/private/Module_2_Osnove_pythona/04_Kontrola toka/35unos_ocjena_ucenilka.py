'''Unesi 5 ucenika i svakome unesi 3 ocjene preko tipkovnice'''

ucenici_i_ocjne = {}

for i in range(2):
    kljuc = input(f'Unesi ime {i+1}. ucenika:')
    lista_ocjena = []
    for j in range(3):
        vrijednost_ocjene = int(input(f'Unesi {j+1}. ocjenu: ')) 
        lista_ocjena.append(vrijednost_ocjene)
    ucenici_i_ocjne[kljuc] = lista_ocjena


print('Ocjene ucenika:')
for kljuc,vrijednost in ucenici_i_ocjne.items():
    print(f' {kljuc} {vrijednost}')
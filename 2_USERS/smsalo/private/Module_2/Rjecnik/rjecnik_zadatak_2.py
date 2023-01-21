#unosimo 5 učenika (imena) preko tipkovnice, svakom učeniku unosimo po 3 ocjene i na kraju ispisujemo dobiveni rječnik

ucenici_ocjene = {}

for i in range(5):
    ime = (input(f'Unesi ime {i+1} učenika: '))
    lista_ocjena = []
    for j in range(3):
        ocjena = int(input(f'Unesi {j+1} ocjenu: '))
        lista_ocjena.append(ocjena)
        ucenici_ocjene[ime]= lista_ocjena
print(ucenici_ocjene)

for k, v in ucenici_ocjene.items():
    print(f'{k}:{v}')

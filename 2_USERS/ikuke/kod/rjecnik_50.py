

#metode nad rječnikom

zivotinje={
    1: 'pas',
    2: 'lav',
    3: 'ris',
    4: 'konj',
    5: 'slon'
}

print (zivotinje)
#clan5= zivotinje.popitem() "vraca n-torku (tuple)"

#print(clan5)


zivotinje.pop(3) #uklanja par s ključem navedenim u zagradi

print (zivotinje)


zivotinje.clear()
print (zivotinje)

del zivotinje


# unos s tipkovnice i ključ i vrijednosti, unaprijed zadamo broj članova rječnika (parova ključ-vrijednost) - unosimo 5 parova
"""
for i in range (5):
    kljuc=input (f'Unesi ime {i+1}. učenika:')
    lista_ocjena=[]
    for j in range (3):
        vrijednost = int(input(f'unesi {j}. ocjenu učenika:'))
        lista_ocjena.append(vrijednost)
    ucenici_ocjene[kljuc]= lista_ocjena

print (ucenici_ocjene)

print ('Učenici      Ocjene')

for k, v in ucenici_ocjene.items():
    print(f'{k}       :   {v}')
"""

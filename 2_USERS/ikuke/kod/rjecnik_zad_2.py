#unosimo ime s tipkovnice i tri ocjene za svakog učenika
#unosimo podatke za 5 učenika

#ispisujemo rječnik

rjecnik={}
ucenici_ocjene={}


# unos s tipkovnice i ključ i vrijednosti, unaprijed zadamo broj članova rječnika (parova ključ-vrijednost) - unosimo 5 parova

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



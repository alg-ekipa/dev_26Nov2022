# a)izračunati prosječnu visinu, b)popis redni br i ime , c) br. učenika i učenica (m i ž) punom rečenicom
ucenici = {
    1 : ['Marko Markić', 'Unska 2, Zagreb', 'M', 1.68],
    2 : ['Ana Anić', 'Krivi put 5, Krapina', 'Ž', 1.55],
    3 : ['Pero Perić', 'Splitska 98, Sinj', 'M', 1.80],
    4 : ['Ivan Ivić', 'Jablanova 3, Sisak', 'M', 1.75],
    5 : ['Stjepan Stjepić', 'Brezova 23, Osijek', 'M', 1.85],
    6 : ['Sara Sarić', 'Otočna 28, Split', 'Ž', 1.61],
    7 : ['Marija Marić', 'Riječna 22, Rijeka', 'Ž', 1.59],
    8 : ['Petra Pertrić', 'Desna 54, Đakovo', 'Ž', 1.68],
    9 : ['Edo Edić', 'Kozuraška 21, Zagreb', 'M', 1.78],
    10 : ['Ante Antić', 'Lijeva 18, Imotski', 'M', 1.80]
}


visina_ucenika = []
for vrijednost in ucenici.values():
    visina_ucenika.append(vrijednost[-1])

prosjecna_visina = sum(visina_ucenika) / len(visina_ucenika)

print(f'Prosječna visina učenika u razredu je: {prosjecna_visina}cm')

print()

lista_rbr =[]
for kljuc in ucenici.keys():
    lista_rbr.append(kljuc)

lista_imena = []
for vrijednost in ucenici.values():
    lista_imena.append(vrijednost[0])

for i in range(len(lista_rbr)):
    print(f'{lista_rbr[i]} : {lista_imena[i]}')

print()

lista_spol = []
for vrijednost in ucenici.values():
    lista_spol.append(vrijednost[2])
broj_M = lista_spol.count('M')
broj_Z = lista_spol.count('Ž')

print(f'Broj učenika je {broj_M}, a broj učenica {broj_Z}.')

'''print(type(lista_rbr)) #otkriva koja je klasa podataka'''
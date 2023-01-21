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
# prosječna visina učenika
lista_visine = []
lista_vrijednosti = ucenici.values()
for visina in lista_vrijednosti:
    lista_visine.append(visina[3])
print(f'Prosječna visna učenika iznosi {sum(lista_visine) / len(lista_visine)}')

# popis u kojem se nalazi redni broj i ime
for kljuc, vrijednost in ucenici.items():
    print(kljuc, ":", vrijednost[0])

#spol učenika
spol = []
lista = ucenici.values()

for vrijednost in lista:
    spol.append(vrijednost[2])
print(spol)

broj_M = spol.count("M")
broj_Z = spol.count("Ž")
print(f'Broj muških učenika je {broj_M}, ženskih {broj_Z}.')


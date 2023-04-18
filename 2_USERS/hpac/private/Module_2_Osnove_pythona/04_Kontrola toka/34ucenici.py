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

rjecnik_ucenika = {
    1 : ['Pero', 5],
    2 : ['Marko', 3],
    3 : ['Iva', 5],
    4 : ['Ante', 2],
    5 : ['Ana', 3]
}

'''
Prosjecnu visinu svih ucenika
popis samo redni broj i ime
broj ucenika i ucenica '''

broj_m = 0
broj_z = 0
lista_visina = []

for kljuc,vrijednost in ucenici.items():
    print(f' {kljuc} {vrijednost[0]}')
    if ucenici[kljuc][2] == 'M':
        broj_m += 1
    if ucenici[kljuc][2] == 'Ž':
        broj_z += 1
    lista_visina.append(ucenici[kljuc][3])
    
print(f'Broj ucenika sa Ž spola je: {broj_z}, a M spola je {broj_m}')

prosjecna_visina = sum(lista_visina)/len(lista_visina)
print(f'Prosjecna visina ucenika je: {prosjecna_visina}')
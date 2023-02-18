#a) iZračunajte prosječnu visinu svih učenika
#b)Napravite popis u kojem će se vidjeti samo redni broj i i me
#c)Ispišite broj učeniak i učenica(M i Ž) punom rečenicom

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
'''
rjecnik_ucenika = {
    1 : ['Pero', 5],
    2 : ['Marko', 3],
    3 : ['Iva', 5],
    4 : ['Ante', 2],
    5 : ['Ana', 3]
}

visina_ucenika=[]
lista_visina=ucenici.values() 
print(lista_visina)

for visina in lista_visina:
    visina_ucenika.append(visina[-1])
    print(visina_ucenika)

prosjecna_visina=sum(visina_ucenika)/len(visina_ucenika)
print(f'Prosječna visina svih učenika je:  {visina_ucenika}')
'''

lista_rbr=[]
for kljuc in ucenici.keys():
    lista_rbr.append(kljuc)
#print(lista_rbr)

lista_imena=[]
for vrijednost in ucenici.values():
    lista_imena.append(vrijednost[0])
    #print(lista_imena)
for i in range(len(lista_rbr)):
     print(f'{lista_rbr[i]}. {lista_imena[i]}')

     lista_spol=[]
     broj_M=lista_spol.count('M')

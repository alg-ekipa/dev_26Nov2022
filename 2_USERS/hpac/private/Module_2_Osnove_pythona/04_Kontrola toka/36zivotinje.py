'''
definiraj reijecnik i testiraj brisanja

'''
zivotinje ={
    1 : ['Pas'],
    2 : ['Osa'],
    3 : ['Ris'],
    4 : ['Kit'], 
    5 : ['Lav']
}

print(zivotinje)

'''uklanja zadnji clan u rijecniku'''
clan5 = zivotinje.popitem() #uzma zadnji clan
print(clan5) # nTorka kljuc i rijec
print(zivotinje) # nema vise tog clana


zivotinje.pop(3) #navedemo koji kljuc da makne
print(zivotinje)

zivotinje.clear #prazni rijecnik
print(zivotinje)

del zivotinje # brise rijecnik
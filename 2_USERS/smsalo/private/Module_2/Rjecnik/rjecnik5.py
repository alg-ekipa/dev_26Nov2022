zivotinje = {
    1: 'pas',
    2: 'lav',
    3: 'ris',
    4: 'konj',
    5: 'slon'
 }

print(zivotinje)

'''
clan5=zivotinje.popitem() #vraća n-torku (tupple) i briše zadnji član iz rječnika 
print(clan5)
print(zivotinje)
'''

clan3=zivotinje.pop(3) #uklanja par s navedenog mjesta
print(clan3)
print(zivotinje)

zivotinje.clear() #obriše podatke iz rječnika, ali rječnik ostaje postojati
print(zivotinje)

del zivotinje  #obriše cijeli rječnik kao varijablu i on više ne postoji
print(zivotinje)
zivotinje = {
    1: 'pas',
    2: 'lav',
    3: 'ris',
    4: 'konj',
    5: 'slon'
}

print(zivotinje)

#clan5 = zivotinje.popitem() #vraća n-torku (tuple), sprema u varijablu, a za zadnji par u rječniku uklanja

#print(clan5)
#print(zivotinje)

zivotinje.pop(3) #uklanja par s ključen navedenim u zagradi

print(zivotinje)

zivotinje.clear() #očisti cijeli rječnik (podatke iz njega)
print(zivotinje)

del zivotinje #obriše cijeli rječnik kao varijablu
print(zivotinje)
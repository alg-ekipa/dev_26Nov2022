zivotinje = {
    1 : 'pas',
    2 : 'lav',
    3 : 'ris',
    4 : 'konj', 
    5 : 'slon'
}



print(zivotinje)

'''
clan5 = zivotinje.popitem() # popitem vraća n-torku (tuple), sačuvao ju je u dodjeljenoj varijabli i maknuo iz rječnika (zadnji par u riječniku)

print(clan5)'''

zivotinje.pop(3) #u zagrdama navodimo ključ para koji želimo ukloniti

print(zivotinje)

zivotinje.clear() #riječnik još uvijek postoji ali je prazan
print(zivotinje)

del zivotinje #briše cijeli rječnik iz memorije



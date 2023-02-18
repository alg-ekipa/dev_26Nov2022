zivotinje={
    1:'pas',
    2:'lav',
    3:'ris',
    4:'konj',
    5:'slon'
}
print(zivotinje)

#clan5=zivotinje.popitem() #vraćan-torku(tuple), sprema u varijablu, a zadnji par u rječniku uklanja

#print(clan5)
#print(zivotinje)

zivotinje.pop(3) #uklanja par s ključem navedenim u zagradi

print(zivotinje)

zivotinje.clear()
print(zivotinje)

del zivotinje
print(zivotinje)
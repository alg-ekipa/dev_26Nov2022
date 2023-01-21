nasa_lista = [154, "tekst", "još jedan tekst", 3.14, True,"pa opet tekst"]

print (nasa_lista)

print(f'prvi član naše liste je {nasa_lista[0]}, a četvrti član {nasa_lista[3]}')
umnozak=nasa_lista[1]
print(umnozak)

zadaci=[
    'Odabrati naziv liste',
    'Unijeti elemente liste',
    'pokrenuti aktivnosti',
]

print(zadaci)
print(zadaci[0])
print(zadaci[1])
print(zadaci[2])


for i in range(100,1,-5):
    print(i, end=" ")

print()
print()
zbroj=0
for i in range(1,21,1):
    zbroj=zbroj+i
    print(i, zbroj)
print ('zbroj brojeva 1 do', i , 'je jednak', zbroj )

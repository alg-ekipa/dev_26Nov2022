# provjera da li je rijec palindrom 
'''
rijec=input('Unesi riječ: ')
obrnuta_rijec=rijec[::-1]
if rijec==obrnuta_rijec:
    print('Unesena rijec je palindrom.')
else:
    print('Unesena rijec nije palindrom.')
'''

# sa while petljom

while True:
    rijec=input('Unesite rijec: ')
    obrnuta_rijec=rijec[::-1]
    if not rijec:
        break
    if rijec==obrnuta_rijec:
        print(f'Unesena riječ {rijec} je palindrom.')
    else:
        print(f'Unesena riječ {rijec} nije palindrom.')

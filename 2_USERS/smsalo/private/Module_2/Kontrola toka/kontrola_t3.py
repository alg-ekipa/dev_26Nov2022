# da li je riječ palindrom

rijec=input('Unesi riječ: ')
obrnuta_rijec=rijec[::-1]

if obrnuta_rijec==rijec:
    print(f'Riječ {rijec} je palindrom.')
else:
    print(f'Riječ {rijec} nije palindrom.')

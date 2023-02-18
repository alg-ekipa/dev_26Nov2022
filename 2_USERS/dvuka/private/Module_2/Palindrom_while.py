rijec=input('Unesi rijeČ: ')

obrnuta_rijec=rijec[::-1]
#print(obrnuta_rijec)

if obrnuta_rijec==rijec:
    print('Riječ je palindrom!')
else:
    print('Riječ NiJE palindrom')

# sa while petljom

while True:
    rijec=input('Unesi riječ: ').lower()

    obrnuta_rijec=rijec[::-1]

    if not rijec:
        break

    if rijec==obrnuta_rijec:
        print(f'Riječ {rijec} je palindrom')
    else:
        print(f'Riječ {rijec} nije palindrom')
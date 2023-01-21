'''

rijec =input('Unesi riječ: ')
obrnuta_rijec = rijec[::-1]
#print(obrnuta_rijec)
if obrnuta_rijec == rijec:
    print('Riječ je palindrom!')
else:
    print('Riječ NIJE palindrom')
'''

while True: 
    rijec =input('Unesi riječ: ').lower()
    obrnuta_rijec = rijec[::-1]
    if not rijec: #ako nismo unijeli ništa
        break

    if rijec == obrnuta_rijec:             #ako smo unijeli riječ prvjeri jeli palindrom
        print('Riječ je palindrom!')
    else:
        print('Riječ NIJE palindrom')

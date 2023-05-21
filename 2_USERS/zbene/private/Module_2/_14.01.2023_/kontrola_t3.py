# PALINDROM (slide 95, 04dio 02 osnove programiranja)

#rijec = 'Zagreb'
#print (rijec [::-1])

rijec = input ('Unesi riječ: ')
obrnuta_rijec = rijec [::-1]
if obrnuta_rijec == rijec:
    print ('Riječ je palindrom!')
else:
    print('Riječ nije palindrom')

#sa while petljom - riječ unosimo sve dok ne stisnemo Enter, odnosno ne unesemo ništa

while True:
    rijec = input ('Unesi riječ ').lower()

    o_rijec = rijec [::-1]

    if not rijec:       #ako nismo unijeli ništa
        break

    if rijec == o_rijec:
        print(f'Riječ {rijec} je palindrom')
    else:
        print(f'Riječ {rijec} nije palindrom')
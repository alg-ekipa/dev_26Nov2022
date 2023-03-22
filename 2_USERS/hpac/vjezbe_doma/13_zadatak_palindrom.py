# napiši program koji provjerava da li je riječ palindrom (jednako se piše lijevo i desno)

while True:
    rijec = input('Unesi riječ: ').lower()

    obrnuta = rijec[::-1]

    if not rijec:
        break
    if rijec == obrnuta:
        print('Riječ je PALINDROM')
    else:
        print('Riječ nije PALINDROM')
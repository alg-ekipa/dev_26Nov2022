rijec =input('Unesi riječ: ')
obrnuta_rijec = rijec[::-1]
while True: 
    if obrnuta_rijec == rijec:
        print('Riječ je palindrom!')
    else:
        print('Riječ NIJE palindrom')
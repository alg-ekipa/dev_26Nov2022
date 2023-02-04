
def provjera(rijec):
    obrnuta_rijec = rijec[::-1]
    if obrnuta_rijec == rijec:
        print('rijec je palindron')
    else:
        print('rijec nije palindron')


rijec = input('unesi rijec:')
provjera(rijec)
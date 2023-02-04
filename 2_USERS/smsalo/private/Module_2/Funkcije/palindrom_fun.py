def palindrom(rijec):
    obrnuta_rijec=rijec[::-1]
    if rijec==obrnuta_rijec:
        print(f'Unesena riječ {rijec} je palindrom.')
    else:
        print(f'Unesena riječ {rijec} nije palindrom.')
    return rijec, obrnuta_rijec

rijec_unos=input('Unesite rijec: ').lower()
palindrom(rijec_unos)



while True:
    rijec = input('Unesi riječ:').lower()

    obrnuta_rijec = rijec[::-1]

    if not rijec:  # Ako nismo unijeli ništa
        break
    if rijec == obrnuta_rijec:      # Ako smo unijeli riječ, provjeri da li je palindrom
        print(f'Riječ {rijec} je palindrom.')
    else:
        print(f'Riječ {rijec} nije palindrom.')
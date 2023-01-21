tonovi=['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'H']
tonovi.extend(tonovi)
#print(tonovi)

while True:
    ton_0=input('Unesi početni ton ')
    
    while ton_0.upper() not in tonovi:
        ton_0=input('Unijeli ste krivo! Unesite pocetni ton: ')
    else:
        pocetni=ton_0.upper()
        pocetni_mol=ton_0.lower()
        #print(pocetni)
        broj=tonovi.index(pocetni)
        #print(broj)
        broj_3=broj+2
        broj_4=broj+3
        broj_7=broj+6
        #print(broj_3, broj_4, broj_7)

        ton_3=tonovi[broj_3]
        ton_4=tonovi[broj_4]
        ton_7=tonovi[broj_7]

        print(f'Za unešeni početni ton', pocetni, 'ljestvica', pocetni, 'dur se sastoji od tonova:', pocetni, ton_4, ton_7)
        print(f'Za uneseni početni ton', pocetni, 'ljestvica', pocetni_mol, 'mol se sastoji od tonova:', pocetni, ton_3, ton_7)

    odluka=input('Zelite li nastaviti unositi akorde? Za DA unesite 1, za NE unesite 0. ')
    if odluka=='0':
        break
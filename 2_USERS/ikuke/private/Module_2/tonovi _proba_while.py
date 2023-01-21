
#tonovi s while petljom za unos


tonovi=['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'H']


tonovi.extend(tonovi)


#printanje(tonovi)

while True:
    ton_POCETNI=input('Unesi početni ton ')
    
    while ton_POCETNI.upper() not in tonovi:
        ton_POCETNI=input('Unijeli ste krivo! Unesite pocetni ton: ')
    else:
        pocetni=ton_POCETNI.upper()
      
        pocetni_mol=ton_POCETNI.lower()
      
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

        print(f'Za početni ton', pocetni, 'ljestvica', pocetni, 'dur se sastoji od tonova:', pocetni, ton_4, ton_7)
        print(f'Za početni ton', pocetni, 'ljestvica', pocetni_mol, 'mol se sastoji od tonova:', pocetni, ton_3, ton_7)

    izbor=input('Zelite li nastaviti unositi akorde? Za DA unesite 1, za NE unesite 0. ')
    if izbor=='0':
        break

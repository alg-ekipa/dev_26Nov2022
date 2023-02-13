"""
MODUL               Modul 2 - Osnove programiranja u Pythonu
TEMA                Varijable i tipovi podataka
NASLOV              KOLEKCIJE PODATAKA
                    ZADATAK
"""




# Dajte polaznicima neka razmisle i pokušaju samostalno riješiti ovaj zadatak

# ZADATAK: Napišite program koji kreira akorde na osnovu početnog tona, odnosno note.
    # POJAŠNJENJE
    # Akord se sastoji od tri tona koji se mogu ponavljati.
    # Durski akord čine: početni ton, 4. ton te 7. ton.
        # Označava se samo velikim slovom početnog tona ili velikim slovom početnog tona uz dodatak dur
    # Molski akord čine: početni ton, 3. ton te 7. ton.
        # Označava se samo malim slovom početnog tona ili malim slovom početnog tona uz dodatak mol

    # Glazbena abeceda: C, C#, D, D#, E, F, F#, G, G#, A, A#, H
        # Engleska oznaka za H ton je B pa oni imaju A B C D E F G pa novi krug od A B
    
    # Postoji pojašnjenje u teoriji glazbe zašto je prvi ton C, ali to sada nije važno.

tonovi = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'H']
print('\nLista svih tonova počevši od tona C:')
for ton in tonovi:
    print(ton, end=' ')
print('\n')

while True:

    pocetni_ton = input('Unesite početni ton akorda:\t')
    # PITANJE: Ako korisnik unese C ili D ton, tada je lako riješiti zadatak:
        # samo iz liste uzmemo indeks tag tona, zatim ton s indeksom + 4 pa ton s indeksom + 7.
        # Za molski akord sve istom samo je drugi ton s indeksom + 3, a ne + 4.
        # Međutim, što ako korisnik unese ton H !? 
        # Kako ćemo računati elemente liste od tog indeksa + 4 i + 7 kada ih nema poslije?
    # ODGOVOR: Proširimo listu za još jedan set tonova

    tonovi.extend(tonovi)
    # ILI 
    # note_prosireno = tonovi + tonovi

    # Pronađimo indeks početnog tona, ali u proširenoj listi
    indeks_pocetnog_tona = tonovi.index(pocetni_ton)

    # I jednostavno ispišimo na ekran rješenje
    # Možemo prethodno tonove pohraniti u neke varijable, ali Python nam olakšava pisanje pa ne trebamo
    print(f'\nDurski akord {pocetni_ton} tona čine:\n'
                        f'\t{pocetni_ton} kao prvi ton,\n'
                        f'\t{tonovi[indeks_pocetnog_tona + 4]} kao 4. ton te\n'
                        f'\t{tonovi[indeks_pocetnog_tona + 7]} kao 7. ton.\n'
                        f'\tSimbol akorda je: {pocetni_ton} ili {pocetni_ton} dur\n')

    print(f'\nMolski akord {pocetni_ton} tona čine:\n'
                        f'\t{pocetni_ton} kao prvi ton,\n'
                        f'\t{tonovi[indeks_pocetnog_tona + 3]} kao 3. ton te\n'
                        f'\t{tonovi[indeks_pocetnog_tona + 7]} kao 7. ton.\n'
                        f'\tSimbol akorda je: {pocetni_ton.lower()} ili {pocetni_ton.lower()} mol\n')


    odluka = input('Želite li nastaviti? da / ne: ')
    if odluka == 'ne':
        break

"""
MODUL               Modul 2 - Osnove programiranja u Pythonu
TEMA                Kontrola toka izvršavanja programskog kôda
NASLOV              UVJETNO IZVRŠAVANJE PROGRAMA
                    IF ELIF ELSE ZADACI
"""




# ZADATAK: Napišite program koji provjerava je li unesena riječ palindrom.
    # Palindrom je riječ koja se jednako piše (i čita) s lieva na desno i s desna na lijevo
rijec = input('Upišite rijec za koju mislite da je PALINDROM:\t')

# Sječate se tekst je lista slova pa vrijedi slice, ali tako da kreira novi tekst, NE da postojeći promijeni
obrnuta_rijec = rijec[ : : -1]

if rijec == obrnuta_rijec:
    print(f'Riječ {rijec} JE palindrom.')
else:
    print(f'Riječ {rijec} NIJE palindrom.')



# IGRA POGODI BROJ
# m2_03_kontrola_toka_pogodi_broj.py



# ZADATAK: Prepravite zadatak tako da se sada ispravno ispisuje tabela
    # Kreirajte bazu s vozilima firme. ID svakog retka je cijeli broj, a vrijednosti o vozilu su unutar
    # liste slijedećih podatka: tip, proizvođač, registarska oznaka, godina prve registracije i cijena u EUR.
    # Ispišite cijelu tablicu tako da ID odvojite od ostatka retka TABom, a druge informacije formatirajte
    # tako da prvi red tablice predstavlja naslovni red, a svi ostali su redovi tablice Kao na slici

# Baza je rječnik. Evo primjera s podacima:
vozni_park = {
    1 : ['Kamion', 'Iveco', 'OS 001 ZZ', 2015, 45000.00],
    2 : ['Kamion', 'Iveco', 'OS 002 ZZ', 2015, 47000.00],
    3 : ['Tegljač', 'MAN', 'RI 001 ZZ', 2018, 78000.00],
    4 : ['Tegljač', 'MAN', 'RI 002 ZZ', 2020, 97000.00],
    5 : ['Kombi', 'Mercedes Benz', 'ST 001 ZZ',2013, 12000.00],
    6 : ['Kombi', 'Volkswagen', 'ST 002 ZZ', 2021, 35000.00],
    7 : ['Dostavno vozilo', 'Volkswagen', 'ZG 001 ZZ', 2010, 9000.00],
    8 : ['Dostavno vozilo', 'Volkswagen', 'ZG 002 ZZ', 2010, 9300.00]
}

# HEADER TABLE ROW
print()
print('_' * 90)
header_top_line = f'ID\tTip\t\tProizvodac\tRegistarska\t\tGodina prve\tCijena'
header_bottom_line = f'  \t   \t\t          \toznaka\t\t\tregistracije\t(EUR)'
print(header_top_line, '\n', header_bottom_line)
print('_' * 90, '\n')

# BODY TABLE ROWs
for kljuc, vrijednost in vozni_park.items():
    print(f'{kljuc}', end='\t')
    for element in vrijednost:
        # Prije ispisa trebamo provjeriti je li element tekst ili broj
        if type(element) == str:
            # Ako je tekst i dužina riječi je duža od 9 znakova.
            # koristimo jedan TAB.
            if len(element) > 9:
                print(f'{element}', end='\t') 
            # INAČE koristimo dva taba
            else:
                print(f'{element}', end='\t\t')
        # Ako nije tekst nego je broj, onda koristimo opet dva taba
        # NAPOMENA: Izostavite ovaj cijeli else pa će ostati bez numeričkog dijela prikaza.
            # Pitajte polaznike zašto je to tako?
        else:
            print(f'{element}', end='\t\t')
    
    print()     # I tek sada možemo preći u novi red
print('_' * 90, '\n\n')

# REZULTAT
# __________________________________________________________________________________________
# ID      Tip             Proizvodac      Registarska             Godina prve     Cijena
#                                         oznaka                  registracije    (EUR)
# __________________________________________________________________________________________
# 
# 1       Kamion          Iveco           OS 001 ZZ               2015            45000.0
# 2       Kamion          Iveco           OS 002 ZZ               2015            47000.0
# 3       Tegljač         MAN             RI 001 ZZ               2018            78000.0
# 4       Tegljač         MAN             RI 002 ZZ               2020            97000.0
# 5       Kombi           Mercedes Benz   ST 001 ZZ               2013            12000.0
# 6       Kombi           Volkswagen      ST 002 ZZ               2021            35000.0
# 7       Dostavno vozilo Volkswagen      ZG 001 ZZ               2010            9000.0
# 8       Dostavno vozilo Volkswagen      ZG 002 ZZ               2010            9300.0
# __________________________________________________________________________________________


# ZADATAK: Ispis radi super, ali dobili smo upit da pošaljemo informaciju koliko firmu koštaju sva vozila
    # te koje vozilo je najskuplje, a koje najjeftinije 
    # te na osnvu tablie ispisšite u kojem gradu su registrirana ta vozila.





# WHILE PETLJA
    # Isti primjeri
    # FOR I WHILE PETLJA


#KOMBINACIJA IF, WHILE I FOR PETLJI
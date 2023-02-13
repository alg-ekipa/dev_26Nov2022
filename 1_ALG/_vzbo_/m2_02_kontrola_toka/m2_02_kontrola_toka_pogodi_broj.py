"""
MODUL               Modul 2 - Osnove programiranja u Pythonu
TEMA                Kontrola toka izvršavanja programskog kôda
NASLOV              ZADATAK WHILE i IF PETLJE
"""



### POGODI BROJ ###
# Sjećate se Računalnog razmišljanja i pogađanja broja između 1 i 100. Sada imate dovoljno znanja da napišete
# program koji će Vam omogućiti pogađanje broja
import random

zamisljeni_broj = random.randint(1, 100) # Od 1 do 100 UKLJUČIVO - nije isto kao range()
broj_pokusaja = 0
while True:
    # Ovu liniju koristiti samo tijekom testiranja, kasnije izbrisati ili komentirati
    print('Zamišljeni broj:', zamisljeni_broj)
    print()
    odgovor = input('Pogodi broj od 1 do 100 koji sam zamislio.\t')
    broj_pokusaja += 1
    
    # NE smijemo zaboraviti broj pretvoriti u broj
    if int(odgovor) == zamisljeni_broj:
        print()
        print('ČESTITAM! To je taj broj koji sam zamislio.')
        print(f'Za to ti je trebalo {broj_pokusaja} pokušaja!')
        print()
        break
    elif int(odgovor) > zamisljeni_broj:
        print(f'Broj je manji od {odgovor}')
    elif int(odgovor) < zamisljeni_broj:
        print(f'Broj je veći od {odgovor}')


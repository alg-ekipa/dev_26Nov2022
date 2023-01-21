"""
MODUL               Modul 2 - Osnove programiranja u Pythonu
TEMA                Kontrola toka izvršavanja programskog kôda
NASLOV              ZADATAK WHILE i IF PETLJE
"""



### KAMEN ŠKARE PAPIR ###
# Napravite program koji će vam omogućiti igrati kamen, škare, papir protiv računala
import random   # Python modul za generiranje nasumičnih brojeva

# Možemo i ovako definirati varijablu tekst
izbornik = """
    Izbornik ocija (upišite broj ispre opcije):
    1. Kamen
    2. Škare
    3. Papir
"""
nastavak= True
while nastavak == True:
    izbor_racunala = random.randint(1, 3)  # Od 1 do 3 UKLJUČIVO - nije isto kao range()
    if izbor_racunala == 1:
        izbor_racunala = 1 #'kamen'
    elif izbor_racunala == 2:
        izbor_racunala = 2 #'skare'
    else:
        izbor_racunala = 3 #'papir'

    print('Izbor racunala', izbor_racunala) # Ovu liniju koristiti samo tijekom testiranja, kasnije izbrisati ili komentirati


    while True:
        print(izbornik)
        izbor_korisnika = int(input('Izaberite: kamen, škare ili papir:\t'))
        if izbor_korisnika == 1:
            izbor_korisnika = 1
            break
        elif izbor_korisnika == 2:
            izbor_korisnika = 2
            break
        elif izbor_korisnika == 3:
            izbor_korisnika = 3
            break
        else:
            print('Pograšan unos! Molimo pokušajte ponovo.')
        

    if izbor_korisnika == izbor_racunala:
        print('NERIJEŠENO! Izabrali se isto kao i računalo')
    elif izbor_korisnika == 1 and izbor_racunala == 3:
        print('Izgubili ste, računalo je odabralo papir')
    elif izbor_korisnika == 1 and izbor_racunala == 2:
        print('POBIJEDILI ste, računalo je odabralo škare')
    elif izbor_korisnika == 3 and izbor_racunala == 2:
        print('Izgubili ste, računalo je odabralo škare')
    elif izbor_korisnika == 3 and izbor_racunala == 1:
        print('POBIJEDILI ste, računalo je odabralo kamen')
    elif izbor_korisnika == 2 and izbor_racunala == 1:
        print('Izgubili ste, računalo je odabralo kamen')
    elif izbor_korisnika == 2 and izbor_racunala == 3:
        print('POBIJEDILI ste, računalo je odabralo papir')

    print('Želite li nastaviti?\n 1) DA\n 2) NE')
    odgovor = int(input())
    if odgovor == 1:
        nastavak = True
    else:
        nastavak = False



# ZADATAK: Prepravite zadatak tako da se ne samo provjera izbora nego i igra ponavlja sve dok kortisnik to želi
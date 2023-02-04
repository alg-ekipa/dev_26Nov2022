#kamen, škare, papir

import random

def kamen_skare_papir():
    ksp=['kamen','škare','papir']
    racunalo=random.choice(ksp)
    #print(racunalo)                 #za testiranje

    igra=1
    br_pobjeda_R=0  #br pobjeda računala
    br_pobjeda_K=0  #br pobjeda korisnika

    while igra:
        korisnik=input('Odaberite: \n kamen \n škare \n papir \n')
        if korisnik in ksp:
            if korisnik==racunalo:
                print(f'Nerješeno! Računalo ima {br_pobjeda_R} pobjede, a vi {br_pobjeda_K} pobjede.' )
            elif korisnik=='kamen' and racunalo=='škare':
                br_pobjeda_K+=1
                print(f'Pobjedili ste! Računalo je odabralo {racunalo}! Računalo ima {br_pobjeda_R} pobjede, a vi {br_pobjeda_K} pobjede.' )
            elif korisnik=='kamen' and racunalo=='papir':
                br_pobjeda_R+=1
                print(f'Izgubili ste! Računalo je odabralo {racunalo}! Računalo ima {br_pobjeda_R} pobjede, a vi {br_pobjeda_K} pobjede.' )
            elif korisnik=='škare' and racunalo=='kamen':
                br_pobjeda_R+=1
                print(f'Izgubili ste! Računalo je odabralo {racunalo}! Računalo ima {br_pobjeda_R} pobjede, a vi {br_pobjeda_K} pobjede.' )
            elif korisnik=='škare' and racunalo=='papir':
                br_pobjeda_K+=1
                print(f'Pobjedili ste! Računalo je odabralo {racunalo}! Računalo ima {br_pobjeda_R} pobjede, a vi {br_pobjeda_K} pobjede.' )
            elif korisnik=='papir' and racunalo=='kamen':
                br_pobjeda_K+=1
                print(f'Pobjedili ste! Računalo je odabralo {racunalo}! Računalo ima {br_pobjeda_R} pobjede, a vi {br_pobjeda_K} pobjede.' )
            elif korisnik=='papir' and racunalo=='škare':
                br_pobjeda_R+=1
                print(f'Izgubili ste! Računalo je odabralo {racunalo}! Računalo ima {br_pobjeda_R} pobjede, a vi {br_pobjeda_K} pobjede.' )

            igra=int(input('Zelite li igrati ponovo? Za DA unesite 1, za NE unesite 0.'))
            if igra==0:
                break
            else:
                racunalo=random.choice(ksp)
        else:
            print('Krivi unos! Pokušajte ponovo: ')

kamen_skare_papir()

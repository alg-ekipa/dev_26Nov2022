#kamen, škare, papir

import random

ksp=['kamen','škare','papir']
racunalo=random.choice(ksp)
print(racunalo)                 #za testiranje

igra=input('Koliko puta želite igrati igru? Unesite BROJ:\n')
br_pobjeda_R=0  #br pobjeda računala
br_pobjeda_K=0  #br pobjeda korisnika
br_igre=1


while int(igra)>0 and igra.isdigit()==True:
    igra=int(igra)
    while br_igre<=igra:
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

            br_igre+=1
            racunalo=random.choice(ksp)
    else:
        break
else:
    print('Krivi unos! Pokušajte ponovo: ')

    
        

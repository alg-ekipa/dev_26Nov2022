"""
MODUL               Modul 2 - Osnove programiranja u Pythonu
TEMA                Kontrola toka izvršavanja programskog kôda
NASLOV              UVJETNO IZVRŠAVANJE PROGRAMA
                    IF ELIF ELSE
"""




# Jako često koristimo uvjete kako bismo kontrolirati tijek događaja. Recimo, kada dođete u banku
# i želite podići neki iznos novca. Ako imate dovoljno na računu i odobren minus, onda ćete dobiti novac,
# a ako nemate dobit ćete ispirku da nemate dovoljno novaca na računu i da vam ne mogu isplatiti trženi iznos.

# Već smo se susreli s Boolean tipom podataka čije vrijednosti su True ili False i nema trećeg.
# Ili crno ili bijelo, nema sivog.

# Analogno primjeru iz banke u programskim jezicima imamo petlje koje ovisno o uvjetu 
# određuju tijek izvršavanja programa. To je IF ELSE petlja i u svim programskim jezicima imaju istu logiku.
# AKO (IF) je uvjet ispunjen (njegova vrijednost je True), tada izvrši blok instrukcija
# INAČE (ELSE) izvrši drugi blok instrukcija.

# Međutim, prije nego nasavitmo dalje sa sintaksom IF telje, trebamo pojasniti neke logicki izraze
# koji se koriste kod kod provjere uvjeta. 
# Nećemo uvijek imati jednu varijablu koja je True ili False, nego ćemo često trebati usporediti dvije varijable
# te ovisno o rezultatu usporedbe, odrediti smjer izvršavanja programa.

# Za to nam koristi tablica logičkih izraza u kojoj su navedeni rezultati "i" (AND) te "ili" (OR) logičkih izraza.
# Tabela logickig izraza
"""
A           B           A and B     A or B
True        Ture        True        True
True        False       False       True
False       True        False       True
False       False       False       False
"""
### SAVJET: Skraćeno tabelu gledamo na slijedeći način ###
# Za izraz AND vrijedi, rezultat je TRUE, AKO SU SVI elementi (i A i B i svi ostali ako ih ima) TRUE
    # ako je bilo koji element FALSE, cijeli izraz je FALSE
# Za izraz OR vrijedi, rezultat je TRUE, AKO je BILO KOJI element (i A i B i svi ostali ako ih ima) TRUE
    # ako su svi FALSE, onda je i cijeli izraz FALSE

# IF petlja kao i FOR ima svoj blok instrukcija pa onda na kraju dolazi : znaak.
# Primjer
prvi_uvjet = True
drugi_uvjet = False
treci_uvjet = True

# Jednostavni primjer
if prvi_uvjet:
    # izvrsi instrukcije SAMO AKO je prvi_uvjet točan ili ima vrijednost True
    pass    # ključna riječ pass, znači nastavi dalje i koristi se u ovakvim i sličnim primjerima
            # kada nemamo nikakav kôd za izvršiti, a moramo napisati nešto, odnosno ne možemo ostaviti prazno
            # također i kod blokova koji će biti odrađeni kasnije, a da ne bi remetili razvoj drugih blokova
            # dodaje se komentar TODO i u novom redu pass. To je znak da trebamo taj dio još završiti
else:
    # AKO prethodni uvjet NIJE ispunjen, odnosno njegova vrijednost je FALSE 
    # TADA BEZ obzira na UVJETE I VRIJEDNOSTI IZVRŠI aktivnosti iz ovog bloka
    pass


# Niz IF uvjeta prije ELSE.
# Ako poslije IF uvjeta trebamo napraviti još jednu provjeru tada bi pisali ELSE IF uvjet, 
# a u Pythonu je to skraćeno i piše se ELIF (kao jedna riječ) poslije koje dolazi novi uvjet
if prvi_uvjet:
    # izvrsi instrukcije SAMO AKO je prvi_uvjet točan ili ima vrijednost True
    pass    # ključna riječ pass, znači nastavi dalje i koristi se u ovakvim i sličnim primjerima
            # kada nemamo nikakav kôd za izvršiti, a moramo napisati nešto, odnosno ne možemo ostaviti prazno
            # također i kod blokova koji će biti odrađeni kasnije, a da ne bi remetili razvoj drugih blokova
            # dodaje se komentar TODO i u novom redu pass. To je znak da trebamo taj dio još završiti
elif drugi_uvjet:
    # Ako prvi uvjet NIJE zadovoljen, znači da je prvi_uvjet NEtočan ili ima vrijednost False
    # Tada je izvršpavanje programa došlo do ove linije pa OPET slijedi provjera
    # AKO je drugi_uvjet točan ili ima vrijednost True izvrši instrukcije u ovom bloku
    pass
elif treci_uvjet:
    # isto kao i za drugi uvjet
    pass
else:
    # AKO niti jedan od uvjeta NIJE ispunjen, odnosno svi su FALSE 
    # TADA BEZ obzira na UVJETE I VRIJEDNOSTI IZVRŠI aktivnosti iz ovog bloka
    pass

# ELSE najčešće koristimo kao slučaj koji pokriva sve one uvjete koje nismo naveli ili nema smisla navoditi.

# ZADATAK: Kreirajte listu od 1 do broja 30. Ispišite sve brojeve koji su djeljivi s 3, 6 i 9
    # Provjera je li broj djeljiv s nekim drugim radimo pomoću % (modulo) operanda.
    # 15 % 3 NEMA ostatka, odnosno to je 0 pa je 15 djeljiv s 3.
    # 16 % 3 je 1, odnosno NIJE jednak 0 pa 16 NIJE djeljiv s 3.
brojevi = []
for broj in range(1, 31):
    brojevi.append(broj)

for broj in brojevi:
    if broj % 3 == 0:
        print(f'Broj {broj} je djeljiv s 3')
    elif broj % 6 == 0:
        print(f'Broj {broj} je djeljiv sa 6')
    elif broj % 9 == 0:
        print(f'Broj {broj} je djeljiv s 9')
    else:
        print(f'Broj {broj} NIJE djeljiv s 3, 6 ili 9')

# REZULTAT
"""
Broj 0 je djeljiv s 3
Broj 1 NIJE djeljiv s 3, 6 ili 9
Broj 2 NIJE djeljiv s 3, 6 ili 9
Broj 3 je djeljiv s 3
Broj 4 NIJE djeljiv s 3, 6 ili 9
Broj 5 NIJE djeljiv s 3, 6 ili 9
Broj 6 je djeljiv s 3
Broj 7 NIJE djeljiv s 3, 6 ili 9
Broj 8 NIJE djeljiv s 3, 6 ili 9
Broj 9 je djeljiv s 3
Broj 10 NIJE djeljiv s 3, 6 ili 9
Broj 11 NIJE djeljiv s 3, 6 ili 9
Broj 12 je djeljiv s 3
...
"""
# Ovo NIJE dobro zato jer 6 JE djeljiv s 3, ALI I sa 6. Isto vrijedi i za 9 s tim što je 9 još djeljiv i s 9.
# Ali zato 12 je dljeivo s 3 i sa 6, ali NE i s 9.
# PITANJE: Kako ovo riješiti?
# ODGOVOR: OVo je primjer kada nam IF iz kojeg ELIF ne pomaže, nego moramo koristiti IF pa iza njega IF.
    # Razlika je u tome što IF + ELIF + ... + ELSE predstavljaju jednu povezanu cjelinu ili blok.
        # U ovom bloku svaka provjera je "svjesna" rezultata one druge. Ako prva provjera bude
        # ispunjena nakon što se izvrši njen blok, ostali se neće niti provjeravati.
        # Ako je broj djeljiv s 3, onda NE provjeravam je li deljiv sa 6 ili 9.
        # PORUKA PREDAVAČU - Dajte polaznicima neka prvo provjere za 9 pa 6 pa 3. Dobit će opet djelomične rez.
    # Dok IF + IF + IF ... predstavlja odvojene dijelove koji rade svaki za sebe.
        # To znači ako je jedan uvjet ispunjen, svejedno će se provjeravati slijedeći IF.
brojevi = []
for broj in range(1, 31):
    brojevi.append(broj)


for broj in brojevi:
    if broj % 9 == 0:
        print(f'Broj {broj} je djeljiv s 9')
    if broj % 6 == 0:
        print(f'Broj {broj} je djeljiv sa 6')
    if broj % 3 == 0:
        print(f'Broj {broj} je djeljiv s 3')
    else:
        print(f'Broj {broj} NIJE djeljiv s 3, 6 ili 9')

# Sada provjera radi kako treba.
# VAŽNO: Uočite da poslije zadnjeg IF-a koji provjerava djeljivost s 3 dolazi ELSE. 
    # Dakle taj IF i taj ELSE blok su POVEZANI, ali nam to ne remeti izvršavanje programa, 
    # samo toga moramo biti svjesni

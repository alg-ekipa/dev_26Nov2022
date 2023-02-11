"""
MODUL               Modul 2 - Osnove programiranja u Pythonu
TEMA                Kontrola toka izvršavanja programskog kôda
NASLOV              UVJETNO IZVRŠAVANJE PROGRAMA
                    BREAK i CONTINUE za FOR i WHILE petlje i PASS
"""


# Ponekad želimo izvršavanje petlje završiti prije kraja - "nasilno izaći iz petlje".
# Za to imamo ključnu riječ BREAK
# Primjer
# Imamo tekst Python Programer koji će FOR petlja ispisati tako da poslije svakog slova doda razmak
for slovo in 'Python Programer':
    print(slovo, end=' ')
print()

# PITANJE: Što ako želimo da se ptelja prestane izvršavati ako petlja niađe na slovo 'g'?
# ODGOVOR: Dodat ćemo IF uvjet ako je slovo jednako 'g' te ako je uvjet ispunjen izvršiti break.
for slovo in "Python Programer":
    if slovo == 'g':
        break
    print(slovo, end=' ')
print()

# Nakon break naredbe, FOR petlja se više nije izvršavala

# Primjer s WHILE petljom

# Ovakva konstrukcija znači beskonačnu petlju
while True:
    print('Pozdrav iz potencijalno beskonačne WHILE petlje s True uvjetom')

    # Pravimo se da su korisnici fer i da će uvijek unijeti 1 ili 0
    odgovor = int(input('Želite li prekinuti petlju? (Da=1/Ne=0) '))
    if odgovor == 1:
        print('\nViše NIJE potencijalno beskonačne WHILE petlje s True uvjetom.\n Upravo je završila :-) \n\n')
        break
    
    # Može i bez else, ali ćemo ga dodati
    else:
        pass
        # Ili neka druga radnja



# Nekada ćemo biti u situaciji da NE želimo izaći iz petlje, ali isto tako želimo da se jedan ili više ciklusa
# NE izvrši do kraja, nego da se preostali dio instrukcija PRESKOČI i ako su ispunjeni uvjeti započne novi ciklus.
# Za to koristimo naredbu continue
# Uzmimo na primjer ispis riječi Python Programer i umjesto prekida (break) navedemo continue.
for slovo in "Python Programer":
    if slovo == 'g':
        continue
    print(slovo, end=' ')
print()
# Ciklus petlje se izvršavao sve do continue i nakon toga je trebao izvršiti print(slovo, end=' '), ali NIJE
# nego je prešao u novi ciklus. Zato u ispisu nemamo slovo 'g'. Čak nemamo niti mjesto za to slovo, 
# kako da nikada nije niti bilo u riječima.

# Uz ove dvije ključne riječi break i continue ide i pass o kojoj smo već govorili, ali da i nju dodamo.
# Pojednostavljeno, pass možemo smatrati kao komentar koji se izvrši. Program komentare ignorira, kao da ne postoje,
# ali PASS neće ignorirati. Program smatra da ima naredbu za izvršiti, samo što ta naredba ne radi ništa.
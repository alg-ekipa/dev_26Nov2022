"""
MODUL               Modul 2 - Osnove programiranja u Pythonu
TEMA                Kontrola toka izvršavanja programskog kôda
NASLOV              STRING - Tekstualni tip podataka uz IF i FOR petlje
"""



# ZADATAK: U generičkom tekstu 'Lorem ipsum ...' (https://www.lipsum.com/) 
    # pronađite koliko se pojavljuje neka riječ.


# SAVJET: Tekst koji se prostire u više redova i koji želimo dodati u jednu varijablu 
# trebamo staviti između tri navodnika na početku i tri na kraju - kao Docstring ili
# trebamo staviti unutar ( ) običnih zagrada, a svaku liniju otvoriti i zatvoriti navodnicima.
# Postoji još opcija da se na kraju svakog reda doda ESCAPE CHARACTER \ -> Primjer je na kraju ovog zadatka
tekst = ('Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
        'Vivamus cursus nulla arcu, sollicitudin aliquet dui tempus non. '
        'Mauris vitae porttitor erat. Morbi vitae diam et urna volutpat hendrerit. '
        'Donec aliquam velit a venenatis bibendum. '
        'Nullam orci erat, bibendum in aliquam eget, finibus eu massa. '
        'Duis tincidunt turpis eget elementum dapibus. '
        'Fusce congue ac elit gravida faucibus. Pellentesque bibendum suscipit ullamcorper. '
        'Nulla non nibh elementum, aliquet dui ac, pharetra eros. '
        'Quisque vel mollis orci. '
        'Nunc porttitor, risus eu sagittis mollis, lorem mauris varius leo, '
        'faucibus semper dui dui vel est. '
        'Donec rutrum velit vitae ex congue, vitae rhoncus nunc dictum. '
        'Suspendisse imperdiet consequat pellentesque. '
        'Curabitur condimentum eget enim at auctor. '
        'In hac habitasse platea dictumst. Fusce semper id augue non sodales. '
        ' '
        'Cras non dui quam. Mauris porttitor mauris sit amet ligula vestibulum '
        'sodales egestas vitae ligula. Nam eleifend sed turpis accumsan laoreet. '
        'Aliquam vel venenatis nulla, et tristique nunc. '
        'Mauris rhoncus tortor interdum nulla sollicitudin convallis. '
        'Fusce euismod dui non metus finibus, et vehicula risus egestas. '
        'In non fermentum lorem. Proin et magna tellus. '
        'Nullam rhoncus luctus lorem, vel rutrum turpis sollicitudin vel. '
        'Cras sit amet sapien vel orci pretium finibus consectetur eu enim. '
        'Cras eget hendrerit sem. Sed ullamcorper sagittis malesuada. '
        'Aenean auctor turpis quis mi egestas malesuada. '
        'Praesent ac tortor vel odio lacinia tempus.')

    
print('\n', tekst, '\n')

# Naredba tekst.lower() sva velika slova u tekstu prebaci u mala slova. Naredba tekst.upper() radi obrnuto.
tekst_lower = tekst.lower()

# Naredba string.split(znak) prođe kroz cijeli tekst i 
lista_rijeci = tekst_lower.split(' ')
print(lista_rijeci)


### START ### OVAJ DIO NAKNADNO DODATI U DRUGOM KRUGU - Vidi pitanje pred kraj zadatka
# Procisti tekst
for rijec in lista_rijeci:
    # Pokusati prvo maknuti samo tocku pa se dobije 3 puta
    # Ako rijec sadrži tocku manknimo je
    if '.' in rijec:
        # Treba točno odrediti koji element liste ćemo ažurirati
        # Dodjeljivanje vrijednosti nekom elementu liste -> lista[indeks] = vrijednost
        # Naredba   lista_rijeci.index(rijec)  mi pomaže da dobijem indeks elementa kojeg ažuriram
        # Taj indeks onda upisujem između uglatih zagrada   lista_rijeci[lista_rijeci.index(rijec)]
        # Naredbom .replace('što', 'čime') zamjenjujem što s čime 
            # -> rijec.replace('.', '') zamjenjujem točku praznim stringom
            # VAŽNO Prazan string NIJE razmak! Razmak ima vrijednost (vidi ASCI tablicu), ali prazan string NEMA
        lista_rijeci[lista_rijeci.index(rijec)] = rijec.replace('.', '')
    # A ako možda rijec ima zarez maknimo i njega na isti način
    elif ',' in rijec:
        lista_rijeci[lista_rijeci.index(rijec)] = rijec.replace(',', '')
    # else nam NE treba pa ga možemo i izostaviti
### END ### OVAJ DIO NAKNADNO DODATI U DRUGOM KRUGU - Vidi pitanje pred kraj zadatka


# Treba nam varijabla u koju ćemo pohraniti koliko puta se pojavljuje tražena riječ
brojac = 0

trazena_rijec = input('Upisite rijec za koju zelite provjeriti broj ponavljanja.\t')

# SAVJET: Kada uspoređujete tekst kojeg je korisnik unio s nekim tekstom kojeg imate u variajbli iy baze ili weba
    # uvijek oba teksta prebacite u mala ili velika slova tako da ste sigurni da veliko ili malo slovo 
    # neće utjecati na rezultat usporedbe. Definirani tekst smo već prebacili u mala slova
    # ćemo onda i ono što je korisnik unio prebaciti u mala slova i pohraniti u novu varijablu zato
    # što ćemo originalni tekst kojeg je korisnik unio kasnije ispisati na ekran.
trazena_rijec_lower = trazena_rijec.lower()

# Prođem kroz listu riječi i za svaku provjerim je li ista onoj koju je korisnik unio. 
# Ako je ista varijablu brojac povečam za jedan, a ako nije zanemarim i provjeravam slijedeću.
# To ponavljam sve dok ima riječi u listi
for rijec in lista_rijeci:
    if rijec == trazena_rijec_lower:
        brojac += 1

# Kada sam završio ispišem poruku korisniku koliko je puta pronađena tražena riječ
print(f'Rijec {trazena_rijec} se u tekstu ponavlja {brojac} puta.\n')

# PITANJE: Rijec LOREM (nije važno je li velikim ili malim slovima) je u tekstu napisana 4 puta, 
    # a nama ju je program našao samo 2 puta. ZASTO?
# ODGOVOR: Zato jer smo prilikom rastavljanja teksta radili rastavljanje po razmaku pa smo za neke riječi
    # dobili da na kraju imaju točku. To znači da smo uspoređivali lorem. i lorem  (s točkom i onaj bez točke)
    # Dakle, našli smo BUG. Rješenje je da tekst treba dodatno procistiti
    # NAPOMENA: Tek u drugom krugu dodajte dio koji je vezan uz "pročišćavanje teksta"


### PRIMJER S Escape Characterom \
tekst = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
        Vivamus cursus nulla arcu, sollicitudin aliquet dui tempus non. \
        Mauris vitae porttitor erat. Morbi vitae diam et urna volutpat hendrerit. \
        Donec aliquam velit a venenatis bibendum. \
        Nullam orci erat, bibendum in aliquam eget, finibus eu massa. \
        Duis tincidunt turpis eget elementum dapibus. \
        Fusce congue ac elit gravida faucibus. Pellentesque bibendum suscipit ullamcorper. \
        Nulla non nibh elementum, aliquet dui ac, pharetra eros. \
        Quisque vel mollis orci. \
        Nunc porttitor, risus eu sagittis mollis, lorem mauris varius leo, \
        faucibus semper dui dui vel est. \
        Donec rutrum velit vitae ex congue, vitae rhoncus nunc dictum. \
        Suspendisse imperdiet consequat pellentesque. \
        Curabitur condimentum eget enim at auctor. \
        In hac habitasse platea dictumst. Fusce semper id augue non sodales. \
         \
        Cras non dui quam. Mauris porttitor mauris sit amet ligula vestibulum \
        sodales egestas vitae ligula. Nam eleifend sed turpis accumsan laoreet. \
        Aliquam vel venenatis nulla, et tristique nunc. \
        Mauris rhoncus tortor interdum nulla sollicitudin convallis. \
        Fusce euismod dui non metus finibus, et vehicula risus egestas. \
        In non fermentum lorem. Proin et magna tellus. \
        Nullam rhoncus luctus lorem, vel rutrum turpis sollicitudin vel. \
        Cras sit amet sapien vel orci pretium finibus consectetur eu enim. \
        Cras eget hendrerit sem. Sed ullamcorper sagittis malesuada. \
        Aenean auctor turpis quis mi egestas malesuada. \
        Praesent ac tortor vel odio lacinia tempus.'

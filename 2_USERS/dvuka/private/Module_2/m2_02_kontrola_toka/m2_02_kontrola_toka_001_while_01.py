"""
MODUL               Modul 2 - Osnove programiranja u Pythonu
TEMA                Kontrola toka izvršavanja programskog kôda
NASLOV              UVJETNO IZVRŠAVANJE PROGRAMA
                    WHILE petlja
"""




### IF petlja je imala uvjet koji ako je ispunjen bi se izvršio blok programskog kôda te petlje SAMO JEDNOM. 
# Nakon završetka bloka programskog kôda IF petlje, program se nastavlja izvršavati dalje, izvan IF petlje.
# WHILE petlja je slična. Isto tako ima uvjet koji ako je ispunjen, osigurava pokrentanje bloka programskog kôda
# unutar WHILE petlje, ali nakon završetka tog bloka programskog kôda, WHILE petlja će ponoviti provjeru uvjeta.
# Ako je uvjet ispunjen, OPET će se pokrenuti isti blok programskog kôda. 
# I to će se ponavljati SVE DOK (while) je uvjet ispunjen.
# WHILE petlju možemo usporediti s FOR petljom, samo što je uvjet jasno naveden, dok kod FOR petlje je
# uvjet da ima elemenata u kolekciji.

# Ako su FOR i WHILE petlje slične, idemo na jednom primjeru pokazati kako radi while petlja 
# i usporediti je s FOR petljom.
brojevi = []
for broj in range(1,21):
    brojevi.append((broj))

# Ispis elemenata liste pomoću FOR petlje
for broj in brojevi:
    print(broj, end=' ')
# FOR petlja se automatski zaustavlja kada više nema elemenata u listi.
# Mi ne moramo brinuti o tome


# Ispis elemenata liste pomoću WHILE petlje
# Treba nam varijabla koja će služiti za provjeru koliko puta smo ponovili blok while petlje.
brojac = 0

# SVE DOK (while) je brojac manji od broja elemenata liste IZVRŠAVAJ:
while brojac < len(brojevi):
    print(broj, end=' ')
    # Povećaj brojač za 1 u napravi provjeru.
    brojac += 1
    
# PITANJE: Što će se dogoditi ako broja ne povećavamo za 1 prilikom svakog ciklusa izvršavanja bloka while petlje?
# ODGOVOR: Dobit ćemo beskonačnu petlju. Neka, polaznici to probaju. Izveršavanje se saustavlja pomoću CTRL + C

# Sve što vrijedi za IF uvjete, vrijedi i za WHILE uvjete. Potpuno su identični.

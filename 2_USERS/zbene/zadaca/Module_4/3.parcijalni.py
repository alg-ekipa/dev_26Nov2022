'''PARCIJALNI ISPIT - Programiranje u Pythonu
1. Kreirajte projekt unutar foldera SmartKey te u njemu kreirajte jednu datoteku koja će 
predstavljati početnu datoteku za izvršavanje Vašeg programa. Ova aplikacija se 
može dodati u jednu veću aplikaciju tako da možete dodati i __init__.py datoteku.
2. Funkcionalnosti koje program treba imati su:
a. Prikaz korisničkog sučelja kao na shemi niže
i. Početni ekran prikazuje samo gumbe za Pozvoniti i Otključati
b. Gumb Pozvoni otvara ekran s porukom da je zvono aktivirano te da će uskoro 
netko doći i otvoriti vrata
c. Gumb Otključaj otkriva srednji panel u kojem se nalazi ploča za unos PIN-a 
te dio na kojem se ispisuju poruke kao uspješno unesen PIN te Dobro došli 
Ime i prezime osobe čiji PIN je unesen.
d. Ukoliko se unese Admin PIN, onda se otvori novi ekran s pitanjem je li se želi 
pokrenuti administracija sustava. Ako korisnik potvrdi, otkriva se panel s listom 
korisnika koji imaju pravo pristupa u kuću. 
i. Ako je neko ime selektirano, tada su polja za unos popunjena 
informacijama selektirane osobe. Nakon unosa izmjena potrebno je 
kliknuti na spremi, odustani ili izbriši da se osoba makne s popisa.
ii. Osoba može biti aktivna ili neaktivna. Samo aktivna osoba može ući u 
kuću, odnosno otključati vrata
iii. Ako se klikne na odustani i u formu se unesu podaci te klikne na gumb 
Spremi, onda se u sustav doda nova osoba.
e. Sve poruke se prikazuju na okviru za prikaz statusa i poruka.
f. Podaci trebaju biti pohranjeni u SQLite bazu podataka.
'''


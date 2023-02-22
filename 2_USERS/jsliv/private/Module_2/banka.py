import os

korisnici = {
    "00001" :["Auto d.o.o.", "2360000123456789", "50000"],
    "00002": ["Trgovina d.o.o.", "2360000987654321", "100000"], 
}

#print(korisnici)

def novi_korisnik():
    naziv = input("Unesi naziv poduzeća: ")
    racun = input("Unesi broj računa: ")
    saldo = input("Unesi saldo računa: ")
    sifra_korisnika = input("Unesi šifru korisnika, mora sadržavati 5 brojeva: ")
    
    while len(sifra_korisnika) > 5:
        print("Šifra mora sadržavati 5 brojeva.")  
        quit() 
    
    korisnici[sifra_korisnika] = naziv, racun, saldo
    print(korisnici)
novi_korisnik()


def stanje_racuna():
    for kljuc, vrijednost in korisnici.items():
        print(korisnici[kljuc][2])
stanje_racuna()

def uplata():
    
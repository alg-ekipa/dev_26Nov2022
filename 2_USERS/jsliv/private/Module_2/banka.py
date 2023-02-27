import os

korisnici = {
    "00001" :["Mak d.o.o.", "236000012345678", "50000"],
    "00002": ["Sunset d.o.o.", "236000098765432", "100000"], 
}

saldo = {
    "00001":["50000"],
    "00002":["100000"]
}

administrator = {
    "admin": ["Luka Lukic", "98765"]
}
#print(korisnici)

def pregled_korisnika():
    for korisnik in korisnici.values():
        print(korisnik[0], korisnik[1], korisnik[2])
#pregled_korisnika()
print()

def logiranje():
    if username in administrator.keys():
        password = input("Unesi lozinku: ")
        while password != administrator[password][1]:
            print("Pogrešna lozinka, pokušajte ponovo.")
            password = input("Unesi password: ")
        else:
            print(f"Dobrodosli {administrator[username][0]}!")
    else:
        print("Nepostojeće korisničko ime.")
    print()

def novi_korisnik():
    sifra = input("Unesi sifru korisnika: ")
    while len(sifra) != 5:
        print("Sifra korisnika mora sadrzavati 5 znamenki.")
        sifra = input("Ponovo unesi sifru korisnika: ")
    else:
        naziv = input("Unesi naziv poduzeća: ")
        racun = input("Unesi broj računa: ")
        while len(racun) != 15:
            print("Broj računa mora sadržavati 15 znamenki.")
            racun = input("Ponovo unesi broj računa: ")
        saldo = input("Unesi saldo računa: ")
        korisnici[sifra] = [naziv, racun, saldo]
        print()
        print("Korisnici u bazi: ")
        pregled_korisnika()  
#novi_korisnik()
print()

def stanje_racuna():
    for kljuc, vrijednost in korisnici.items():
        print(korisnici[kljuc][2])
#stanje_racuna()
print()

def uplata():
    uplata = float("Upisite iznos za uplatu: ")
    novo_stanje = korisnici[racun][-1] + uplata
    korisnici[racun].append(novo_stanje)
    print(f"Na racunu: {racun} novo stanje je: {novo_stanje} Eur.")
    print()

def isplata():
    isplata = float(input("Upisi iznos koji želite isplatiti: "))
    podizanje_stanje = korisnici[racun][-1] - isplata
    korisnici[racun].append(podizanje_stanje)
    print(f"Na racunu {racun} sada se nalazi {podizanje_stanje} Eur.")
    print()

def prikaz_prometa():
    a = len(korisnici[racun]) -1
    for i in range(a, 2, -1):
        print(f"\t\tStanje:\t\tUplata/isplata:\n\t\t{korisnici[racun][i]} eura\t\t {korisnici[racun][i]-korisnici[racun][i-1]} Eur.')")


while 1:
    prijava = input("Želite se prijaviti? da/ne: ")
    if prijava == "da":
        login = input("Unesite korisničko ime administratora: ")
        logiranje(login)
        while True:
            izbornik = int(input("Odaberite opciju:\n1. Pregled korisnika\n2. Uplata\n3. Isplata\n4. Novi korisnik\n5. Odjava\n-----> "))
            if izbornik == 1:
                pregled_korisnika()
            elif izbornik == 2:
                uplata()
            elif izbornik == 3:
                isplata()
            elif izbornik == 4:
                novi_korisnik()
            elif izbornik == 5:
                quit()
            else:
                print("Niste odabrali valjanu opciju.")
                izbornik = int(input("Odaberite opciju:\n1. Pregled korisnika\n2. Uplata\n3. Isplata\n4. Novi korisnik\n5. Odjava\n-----> "))
            

    


            
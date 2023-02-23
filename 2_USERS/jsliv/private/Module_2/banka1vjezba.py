import os
class bcolors:
    OKGREEN = '\033[92M'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

vrsta_korisnika = ["a", "r", "k"]

klijenti = {
    'admin': ['Ivan', 'Ivic', 'admin123', 1989, 'a'],
    'referent': ['Luka', 'Lukić', 'pult123', 1973, 'r'],
    'ppetric' : ['Petar', 'Petrić', 'pero123', 1953,'k'],
    'mmarkic' : ['Marko', 'Markić', 'marc123', 1923, 'k'],
    'rrokic' : ['Roko', 'Rokić', 'roko123', 2015, 'k']
}

racuni_klijenata = {
    'a': [10, 20, 35.5, 5, 8, 13, 5,8],
    'referent': [8,5,6,4,1,2,5,3,25,],
    'ppetric' : [85,25,65,8.5,63,25],
    'mmarkic' : [100,25,125,1258.8,10,85],
    'rrokic' : [9,8,56,25,14,12,12.5,25.4]
}

klijenti_izbrisani = {
    'test1' : ['Proba', 'Probic', 'proba123', 1234, 'k']
}
racuni_klijenata_izbrisani = {
    'test1' : []
}

def provjera_korisnika(klijent):
    while klijent not in klijenti.keys():
        print(bcolors.FAIL + "\n\tKorisničko ime ne postoji u bazi." + bcolors.ENDC)
        klijent = input("\tUpišite ispravno korisničko ime: ")
    return klijent

def provjera_lozinke(uneseno_korisnicko, uneseni_pswd):
    while uneseni_pswd != klijenti[uneseno_korisnicko][2]:
        print(bcolors.FAIL + "\n\tKrivo ste unjeli lozinku!" + bcolors.ENDC)
        uneseni_pswd = input("\tUpišite ispravnu lozinku: ")

def brojanje_tocke(iznos):
    if iznos.count(".") + iznos.count(",") == 1:
        iznos = iznos.replace(",",".")
    return iznos

def racun_oduzimanje_novca(klijent, iznos):
    privremena_lista = list(racuni_klijenata[klijent])
    privremena_vrijednost = racuni_klijenata[klijent][-1] - float(iznos)
    privremena_lista.append(privremena_vrijednost)
    racuni_klijenata.update({klijent : privremena_lista})

def racun_dodavanje_novca(klijent_destinacija, iznos):
    privremena_lista = list(racuni_klijenata[klijent_destinacija])
    privremena_vrijednost = racuni_klijenata[klijent_destinacija][-1] + float(iznos)
    privremena_lista.append(privremena_vrijednost)
    racuni_klijenata.update({klijent_destinacija : privremena_lista})

def provjera_svote_za_transfer(iznos, klijent):
    if iznos.count(".") + iznos.count(",") == 1:
        iznos=iznos.replace(",",".")
    while (iznos.count(".") + iznos.count(",")) > 1 or iznos.replace(".","").replace(",","").isdigit() == False or float(racuni_klijenata[klijent][-1]) < float(iznos):
        print("Pogrešan unos.")
        if iznos.replace(".", "").replace(",", "").isdigit() == False:
            iznos = input (bcolors.FAIL+ "Niste upisali broj. Unesite iznos: " +bcolors.ENDC)
            iznos = brojanje_tocke(iznos)
        elif iznos.count(".") + iznos.count(",") > 1:
            iznos = input(bcolors.FAIL + "Upisali ste veći iznos od dozvoljenog" + bcolors.ENDC)
            iznos = brojanje_tocke(iznos)
        return(iznos)
    
    
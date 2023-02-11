korisnici = {
    'admin':['Ivan', 'Ivic', 'aei123'],
    'pperic':['Petar', 'Peric', 'ou456'],
    'mmaric':['Mara','Maric','rst567'],
}

def pregled_korisnici():
    """ Funkcija koja ispisuje sve korisnike iz baza/rječnika """
    for v in korisnici.values():
        print(f' Ime: {v[0]}, Prezime: {v[1]}')





def tko_je_admin():
    """ Funkcija koja ispisuje ime i prezime administratora """
    for k,v in korisnici.items():
        if (k== 'admin'):
            print(f' Ime: {v[0]}, Prezime: {v[1]} -------------------------- je Admin')



def dohvati_admin_pswd():
    for k,v in korisnici.items():
        if k== 'admin':
            return v[2]



def logiranje(uneseni_username):
    if uneseni_username in korisnici.keys():
        uneseni_password= input('unesi lozinku: ')
        if uneseni_password == korisnici[uneseni_username][2]:
            print(f'Dobrodosli, {korisnici[uneseni_username][0] } {korisnici[uneseni_username][1]}')
            
    else:
        print(f'Nepostojeće korisničko ime')

pregled_korisnici()
tko_je_admin()
a=dohvati_admin_pswd()
print('Admin password je ', a)


username=input('Unesi korisničko ime:')
logiranje(username)

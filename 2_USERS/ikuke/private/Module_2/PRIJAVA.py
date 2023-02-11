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


def dodavanje_novog_korisnika_u_listu():
        #punjenje rječnika iz dvije liste - jedna su klučevi, a druga su vrijednosti

    rjecnik_iz_liste = {}

    lista_kljuceva = [1, 2, 3, 4, 5]
    lista_vrijednosti = ['python', 'c++', 'java', 'perl', 'asp.net']

    for i in range (len(lista_kljuceva)):
        kljuc=lista_kljuceva[i]
        vrijednost=lista_vrijednosti[i]
        rjecnik_iz_liste[kljuc]=vrijednost


    for k, v in rjecnik_iz_liste.items():
        print(f'{k} : {v}')




def dohvati_admin_pswd():
    for k,v in korisnici.items():
        if k== 'admin':
            return v[2]


def dodavanje_korisnika():
    odg = input ('Želite li se dodati korisnika? da/ne ')
    if odg == 'da':
        username_korisnika=input('Unesi korisničko ime:')
        ime_korisnika=input('Unesi ime kosrinika:')
        prezime_korisnika=input('Unesi prezime kosrinika:')
        sifra_korisnika=input('Unesi šifru korisnika:')
        print(f'korisnik {ime_korisnika} {prezime_korisnika} ima username {username_korisnika} i šifru {sifra_korisnika}')
        korisnici.update({username_korisnika:['ime_korisnika','prezime_korisnika','sifra_korisnika']})
        
        
    else:
        print('unijeli ste da ne želite dodati novog korinika')



def logiranje(uneseni_username):
    if uneseni_username in korisnici.keys():
        uneseni_password= input('unesi lozinku: ')
        if uneseni_password == korisnici[uneseni_username][2]:
            print('___________________________________________________________________________________')
            print(f'Dobrodosli, {korisnici[uneseni_username][0] } {korisnici[uneseni_username][1]}')
            print('___________________________________________________________________________________')
            
    else:
        print(f'Nepostojeće korisničko ime')

pregled_korisnici()
tko_je_admin()
a=dohvati_admin_pswd()
print('Admin password je ', a)

dodavanje_korisnika()

while 1:
    odg = input ('Želite li se prijaviti? da/ne ')
    if odg== 'da':

        username=input('Unesi korisničko ime:')
        logiranje(username)
        
    else:
        break

pregled_korisnici()
class TV_aparat:
    '''Klasa koja opsiuje TV aparat  - svojstva i radnje'''
    #svojstva (propertise)
    def __init__(self, model, proizvođač, dijagonala, ukljucen=False, program=0, glasnoća=0):
        self.model = model
        self.proizvođač = proizvođač
        self.dijagonala = dijagonala
        self.ukljucen = ukljucen
        self.program = program
        self.glasnoća = glasnoća
    
    #Metode (Funkcije, radnje)
    def ukljuci(self):      #simulira uključivanje TV-a i pritom postavljna na navedene varijable (1. program glasnoća 3)
        self.ukljucen = True
        self.program = 1
        self.glasnoća = 3
    
    def promijeni_program (self, novi_program):     #Postavljenje varijable self.program na novu vrijednost
        self.program = novi_program                 # simulacija promjene program na TV-u

    def podesi_glasnoću (self, nova_glasnoća):       #Postavljenje varijable self.glasnoća na novu vrijednost
        self.glasnoća = nova_glasnoća               # simulacija promjene glasnoće na TV-u

    def ispis_proizvodac(self):
        print(f'Proizvođal TV-a je: {self.proizvođač}')

tv_dnevna_soba = TV_aparat('XY1', 'Sony', 55)
print(f'TV u dnevnoj sobi je marke {tv_dnevna_soba.proizvođač}, i trenutno stanje uključen je: {tv_dnevna_soba.ukljucen}')
tv_dnevna_soba.ukljuci()
print(f'Nakon poziva metode uključi() stanje uključen za TV u dnevnoj sobi je: {tv_dnevna_soba.ukljucen}')

print(f'Trenutna glasnoća TV-a u dnevnoj sobi je {tv_dnevna_soba.glasnoća}')
tv_dnevna_soba.podesi_glasnoću(6)
print(f'Nakon poziva metode za promjenu glasnoća, glasnoća TV-a u snvnoj sobi je {tv_dnevna_soba.glasnoća}')

tv_dnevna_soba.promijeni_program(5)
print(f'Novi program je {tv_dnevna_soba.program}')


#ZADAĆA: instancirati još dva objekta klase TV_apart: soba i ured

# izvaditi sve proizvođače i staviti u listu: Lista_proizvođača

tv_soba = TV_aparat('HR23','Samsung',65)
tv_ured = TV_aparat('TKN1','Philips',75)

lista_televizora = [tv_dnevna_soba, tv_soba, tv_ured]

for tv in lista_televizora:
    tv.ispis_proizvodac()
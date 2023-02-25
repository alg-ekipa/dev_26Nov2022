class TV_aparat:
    '''Klasa koja opisuje TV aparat - svojstva i radnje'''

    #Svojstva (propreties)
    def __init__(self, model, proizvođač, dijagonala, uključen=False, program=0, glasnoća=0):
        self.model = model
        self.proizvođač = proizvođač
        self.dijagonala = dijagonala
        self.uključen = uključen
        self.program = program
        self.glasnoća = glasnoća
    
    #Metoda (funkcije, radnje)
    def uključi (self):             #uključivanje TV-a i pritom postavlja navedene varijable na neke vrijednosti
        self.uključen = True
        self.program = 1
        self.glasnoća = 3

    def promijeni_program (self, novi_program): #postavljanje varijable self.program na novu vrijednost
        self.program = novi_program             #simulacija promjene programa na TV-u

    def podesi_glasnoću (self, nova_glasnoća):  #postavljanje varijable self.glasnoće na novu vrijednost
        self.glasnoća = nova_glasnoća           #simulacija podešavanja glasnoće na TV-u

tv_dnevna_soba = TV_aparat ('XY1', 'Sony', 55)
print(f'TV u dnevnoj sobi je marke {tv_dnevna_soba.proizvođač} i trenutno stanje uključen je {tv_dnevna_soba.uključen}')
tv_dnevna_soba.uključi()
print(f'Nakon poziva metode ukljuci() stanje uključen za TV u dnevnoj sobi je: {tv_dnevna_soba.uključen}!')

tv_dnevna_soba = TV_aparat ('XY1', 'Sony', 55)
print(f'TV u dnevnoj sobi je marke {tv_dnevna_soba.proizvođač} i trenutno je na glasnoći {tv_dnevna_soba.glasnoća}')
tv_dnevna_soba.podesi_glasnoću (8)
print(f'Nakon poziva metode podesi.glasnoću() glasnoća je na TV u dnevnoj sobi: {tv_dnevna_soba.glasnoća}!')

#instancirati još dva objekta klase TV_aparat_ npr. tv_spavaća soba, tv_kuhinja

#izvaditi sve proizvođače i staviti u listu: lista_proizvođača
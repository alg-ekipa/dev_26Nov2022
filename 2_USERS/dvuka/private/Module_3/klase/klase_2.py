class TV_aparat:
    '''Klasa koja opisuje TV aparat-svojstva i radnje'''

    #svojstva(properties)
    def __init__(self, model, proizvodac, dijagonala, ukljucen=False, program=0, glasnoca=0):
        self.model=model
        self.proizvodac=proizvodac
        self.dijagonala=dijagonala
        self.ukljucen=ukljucen
        self.program=program
        self.glasnoca=glasnoca

    #Metode(funckcije, radnje)
    def ukljuci(self):      #uključivanje TV-a i pritom postavlja navedene varijable na neke vrijednosti
        self.ukljucen=True
        self.program=1
        self.glasnoca=3

    def promijeni_program(self, novi_program):  #postavljanje varijable self.program na novu vrijednost
        self.program=novi_program               #simulacija promjene programa na TV-u

    def podesi_glasnocu(self, nova_glasnoca):   #postavljanje varijable self.glasnoca na nvu vrijednost
        self.glasnoca=nova_glasnoca             #simulacij POSEŠAVANJA GLASNĆE  na TV-u

tv_dnevna_soba=TV_aparat('XY1', 'Sony', 55)
print(f'TV u dnevnoj sobi je marke {tv_dnevna_soba.proizvodac}, i trenutno stanje uklučen je {tv_dnevna_soba.ukljucen}')
tv_dnevna_soba.ukljuci()
print(f'Nakon poziva metode ukljuci() stanje ukljucen za TV u dnevnoj sobi je: {tv_dnevna_soba.ukljucen}!')

tv_dnevna_soba.podesi_glasnocu(8)
print(f'Nova glasnoća TV-a u dnevnoj sobi je: {tv_dnevna_soba.glasnoca}')

tv_dnevna_soba.promijeni_program(7)
print(f'Novi program na Tv-u je: {tv_dnevna_soba.program}')

#instancirati još 2 objekta klase TV aparat: npr tv_spavaca_soba, tv_kuhinja

#izvaditi sve proizvođače i staviti u listu:lista proizvođača

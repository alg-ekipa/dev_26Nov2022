class TV_aparat():
    '''Klasa koja opisuje TV aparat - svojstva i radnje'''
    #svojstva 
    def __init__(self, model, proizvodac, dijagonala, ukljucen=False, program=0, glasnoca=0):
        self.model = model
        self.proizvodac = proizvodac
        self.dijagonala = dijagonala
        self.ukljucen = ukljucen
        self.program = program
        self.glasnoca = glasnoca

    #metode (funkcije, radnje)
    def ukljuci(self):      #simulira ukljucivanje TV-a i pritom postavlja navedene varijable
        self.ukljucen = True
        self.program = 1
        self.glasnoca = 3
    
    def promijeni_program(self, novi_program):  #postavljanje varijable self.program na novu vrijednost
        self.program = novi_program        #simulacija promjene programa na TV-u
    
    def podesi_glasnocu(self, nova_glasnoca):      #postavljanje varijable self.glasnoca na novu vrijednost
        self.glasnoca = nova_glasnoca          #simulacija podesavanja glasnoce


tv_dnevna_soba = TV_aparat('Bravo', 'Sony', 55)
print(f' TV u dnevnoj sobi je marke {tv_dnevna_soba.proizvodac} i trenutno stanje ukljucen je: {tv_dnevna_soba.ukljucen}')
tv_dnevna_soba.ukljuci()
print(f'Nakon poziva metode ukljuci() stanje ukljucen u TV sobi je: {tv_dnevna_soba.ukljucen}')


tv_dnevna_soba.podesi_glasnocu(8)
print(f'Nakon poziva metode glasnoca() stanje glasnoce u TV sobi je: {tv_dnevna_soba.glasnoca}')

#inicirati jos dva objekta klase TV_aparat

#izvaditi sve proizvođače i staviti u listu: lista_proizvodaca

tv_spavaca_soba = TV_aparat('X12', 'Philips', 48)
tv_djecja_soba = TV_aparat('A34', 'Toshiba', 32)

lista_proizvodaca = [tv_dnevna_soba.proizvodac, tv_spavaca_soba.proizvodac, tv_djecja_soba.proizvodac ]
print(lista_proizvodaca)
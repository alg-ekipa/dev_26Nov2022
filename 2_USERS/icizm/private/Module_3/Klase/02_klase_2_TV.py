class TV_aparat:
    '''Klasa koja opisuje TV aparat - svojstva i radnje'''

    # Svojstva (properties)

    def __init__(self, model, proizvodac, dijagonala, ukljucen = False, program = 0, glasnoca = 0):
        self.model = model
        self.proizvodac = proizvodac
        self.dijagonala = dijagonala
        self.ukljucen = ukljucen
        self.program = program
        self.glasnoca = glasnoca

    # Metode (funkcije, radnje) 
    def ukljuci(self):                           # Uključivanje TVa i pritom postavlja navedene varijable na neke vrijednosti
        self.ukljucen = True
        self.program = 1
        self.glasnoca = 3

    def promjeni_program(self, novi_program):    # Postavljanje varijable self.program na novu vrijednost
        self.program = novi_program              # simulacija promjene programa na TVu

    def podesi_glasnoću (self, nova_glasnoca):   # Postavljanje varijable self.glasnica na novu vrijednost
        self.glasnoca = nova_glasnoca            # simulacija podešavanja glasnoće na TVu

tv_dnevna_soba = TV_aparat('XY1', 'Sony', 55)
print(f'TV u dnevnoj sobi je marke {tv_dnevna_soba.proizvodac}, i trenutno stanje uključen je {tv_dnevna_soba.ukljucen}!')
tv_dnevna_soba.ukljuci()
print(f'Nakon poziva metode ukljuci() stanje uključen za TV u dnevnoj sobi je: {tv_dnevna_soba.ukljucen}!')

print(f'Trenutno stanje glasnoće na TV u dnevnoj sobi je: {tv_dnevna_soba.glasnoca}')
tv_dnevna_soba.podesi_glasnoću(6)
print(f'Nakon podešavanja glasnoća na TV u dnevnoj sobi je: {tv_dnevna_soba.glasnoca}')

print(f'Trenutni program na TV u dnevnoj sobi je: {tv_dnevna_soba.program}.')
tv_dnevna_soba.promjeni_program(2)
print(f'Nakon podešavanja programa na TV u dnevnoj sobi je: {tv_dnevna_soba.program}.')

# instancirati još dva objekta klase TV_aparat
# izvaditi sve proizvođače i staviti u listu: lista_proizvođača

tv_spavaca_soba = TV_aparat('Najbolji model', 'Sanyo', 60)
tv_kuhinja = TV_aparat('OK model', 'Quadro', 40)

lista_proizvodaca = [tv_dnevna_soba.proizvodac, tv_spavaca_soba.proizvodac, tv_kuhinja.proizvodac]


class TV_aparat:
    """Klasa koja opisuje TV aparat - svojstva i radnje"""
    #Svojstva (properties)

    def __init__(self, model, proizvodac, dijagonala, ukljucen=False, program=0, glasnoca=0):
        self.model = model
        self.proizvodac = proizvodac
        self.dijagonala = dijagonala
        self.ukljucen = ukljucen
        self.program = program
        self.glasnoca = glasnoca
    
    # metode (funkcije, radnje)

    def ukljuci(self):               #uključivanje TVa i protom postavlja navedee varijable na neke vrijednosti
        self.ukljucen = True
        self.program = 1
        self.glasnoca = 3

    def promijeni_program(self, novi_program):     # postavljanje varijable self.program na novu vrijedost
        self.program = novi_program                # simulacija promjene programa na TVu
    
    def podesi_glasnocu(self, nova_glasnoca):      # postavljanje varijable self.glasnoca na novu vrijednost
        self.glasnoca = nova_glasnoca              # simulacija podesavanja glasnoce na TVu

    def podesi_program(self, novi_program):
        self.program = novi_program




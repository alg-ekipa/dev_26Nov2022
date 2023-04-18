class Vozilo:
    def __init__(self, kotaci, mjesta, brzina):
        self.kotaci=kotaci
        self.mjesta=mjesta
        self.brzina=brzina
    
    def vozi(self):
        print('služim za prijevoz')

class Auto(Vozilo):
    def __init__(self):
        super().__init__(4,5,200)

class Bus(Vozilo):
    def __init__(self):
        super().__init__(4, 56, 130)

class Motor(Vozilo):
    def __init__(self):
        super().__init__(2,2,250)

a=Auto()
print(a.kotaci, a.mjesta, a.brzina)
a.vozi()

b=Bus()

print('Max brzina busa je', b.brzina)
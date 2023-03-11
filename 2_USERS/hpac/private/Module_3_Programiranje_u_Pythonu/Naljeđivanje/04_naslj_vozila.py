class Vozilo:
    def __init__(self, kotaci, mjesta, maks_brzina):
        self.kotaci = kotaci
        self.mjesta = mjesta
        self.maks_brzina = maks_brzina

    def vozi(self):
        print('Služim za prijevoz')

class Auto(Vozilo):
     def __init__(self):
        super().__init__(4,5,200)

class Motor(Vozilo):
    def __init__(self):
        super().__init__(2,2,300)

class Bus(Vozilo):
    def __init__(self):
        super().__init__(6, 56, 110)

a = Auto()
print(a.kotaci, a.mjesta, a.maks_brzina)
a.vozi()
m = Motor()
b = Bus()
m.vozi()

print('Max brzina busa je ',b.maks_brzina)
class  Vozila:
    def __init__(self, kotaci, mjesta, max_brzina):
        self.kotaci = kotaci  
        self.mjesta = mjesta  
        self.max_brzina = max_brzina  

    def vozi(self):
        print('Sluzim za prijevoz')

class Auto(Vozila):
    def __init__(self):
        super().__init__(4, 5, 200)

class Motor(Vozila):
    def __init__(self):
        super().__init__(2, 2, 300)

class Bus(Vozila):
    def __init__(self):
        super().__init__(4, 56, 130)

a = Auto()                               # dodjeljivanje Auta u 'a'
print(a.kotaci, a.mjesta, a.max_brzina)  # ispisuje podatke iz klsae Auto
a.vozi()                                 # poziva naredbu iz Parent klase
m = Motor()                             
b = Bus()
m.vozi()                                 # ispisuje podatke iz klsae Auto
print('Max brzina busa je', b.max_brzina)
print('Broj kotaca motora je', m.kotaci)

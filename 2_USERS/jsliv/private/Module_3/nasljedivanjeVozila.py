class Vozilo:
    def __init__(self, kotaci, mjesta, max_brzina):
        self.kotaci = kotaci
        self.mjesta = mjesta
        self.max_brzina = max_brzina
    
    def vozi():
        print("Služi za prijevoz.")

class Auto(Vozilo):
    def __init__(self):
        super().__init__(4, 5, 200)
    

class Motor(Vozilo):
    def __init__(self):
        super().__init__(2, 2, 300)


class Bus(Vozilo):
    def __init__(self):
        super().__init__(10, 50, 180)

a = Auto
print(a.kotaci, a.mjesta, a.max_brzina)
a.vozi()
m = Motor()
b = Bus()
m.vozi()
print("Max brizna busa je", b.max_brzina)
print("Broj kotaca motora je", m.kotaci)
    
class Mnogokut:                         # parent klasa
    def __init__(self,stranice):
        self.stranice = stranice

    def prikaz_info(self):
        print('Mnogokut je 2D lik ravnih stranica.')

    def izracunaj_opseg(self):
        opseg = sum(self.stranice)
        return opseg

class Trokut(Mnogokut):                 # child klasa
    def prikaz_info(self):
        print('Trokut je mnogokut sa 3 kuta')
        Mnogokut.prikaz_info(self) # - bilo koji od ova dva načina radi istu stvar
        #super().prikaz_info()

class Četverokut(Mnogokut):
     def prikaz_info(self):
        print('Četverokut je mnogokut sa 4 kuta')

t1 = Trokut([2,3,4])    # child klasi su dostupne sve metode iz parent klase
t1.prikaz_info()
print('Opseg je ', t1.izracunaj_opseg())

c1 = Četverokut([2,3,4,5])
c1.prikaz_info()
print('Opseg je ', c1.izracunaj_opseg())


class Mnogokut:
    def __init__(self, stranice):
        self.stranice = stranice
    
    def prikaz_info(self):
        print('Mnogokut je 2D lik ravnih stranica')

    def izracunaj_opseg(self):
        opseg = sum(self.stranice)
        return opseg

class Trokut(Mnogokut):
    def prikaz_info(self):
        print ('Trokut je mnogokut s tri kuta')
        Mnogokut.prikaz_info(self)
        super().prikaz_info()

class Cetverokut(Mnogokut):
    def prikaz_info(self):
        print ('Četverokut je mnogokut s četiri kuta')
        Mnogokut.prikaz_info(self)
        super().prikaz_info()



t1 = Trokut([2,3,4])

t4 = Cetverokut([2,3,4,5])

t1.prikaz_info()        

print ('Opseg je ', t1.izracunaj_opseg()) #child klasi su dostupne sve metode iz parent klase

t4.prikaz_info()
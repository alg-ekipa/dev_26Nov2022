class Mnogokut:             #parent klasa
    def __init__(self, stranice):
        self.stranice=stranice

    def prikaz_info(self):
        print('Mnogokut je 2S lik ravnih stranica')

    def izracunaj_opseg(self):
        opseg=sum(self.stranice)
        return opseg

class Trokut(Mnogokut):         #child klasa
    def prikaz_info(self):
        print('Trokut je mnogokut s tri kuta')
        Mnogokut.prikaz_info(self)
        #super().prikaz_info()

class Cetverokut(Mnogokut):
    def prikaz_info(self):
        print('Četverokut je mnogokut s 4 kuta')

t1=Trokut([2,3,4])
t1.prikaz_info()
print('Opseg je', t1.izracunaj_opseg())

c1=Cetverokut([2,3,4,5])
c1.prikaz_info()
print('Opseg je', c1.izracunaj_opseg())

t1=Trokut([2,3,4])
t1.prikaz_info()
print('Opseg je', t1.izracunaj_opseg()) #child klasi su dostupne sve metode iz parent klase

class Mnogokut:
    def __init__(self,stranice):
        self.stranice = stranice

    def prikaz_info(self):
        print ('Mnogokut je 2D lik ravnih stranica.')

    def izračunaj_opseg(self):
        opseg = sum(self.stranice)
        return opseg

class Trokut (Mnogokut):
    def prikaz_info(self):
        print ('Trokut je mnogokut sa tri kuta.')
        Mnogokut.prikaz_info(self) #1. način pozivanja iz glavne
        super().prikaz_info() #2. način pozivanja iz glavne

class Četverokut (Mnogokut):
    def prikaz_info(self):
        print ('Četverokut je mnogokut sa četiri kuta.')

t1 = Trokut ([2,3,4,])
t1.prikaz_info()
print ('Opseg je', t1.izračunaj_opseg(),'cm.') #child klasi su dostupne sve metode iz parent klase
c1 = Četverokut([2,3,4,5])
c1.prikaz_info()
print ('Opseg je', c1.izračunaj_opseg(),'cm.')
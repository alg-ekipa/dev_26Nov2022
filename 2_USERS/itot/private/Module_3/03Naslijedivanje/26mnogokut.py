class Mnogokut:                     #parent klasa

    def __init__(self,stranice):
        self.stranice = stranice

    def prikaz_info(self):              #metoda prikaz info
        print('Mnogokut je 2D lik ravnih stranica')

    def izracujan_opseg(self):          #metoda izracuna opsega
        opseg = sum(self.strancie)
        return opseg
    


class Trokut(Mnogokut):             #child klasa
    
    def prikaz_info(self):
        print('Trokut je mnogokut sa tri kuta')
        super().prikaz_info()                       # prijenosi iz glavne klase
        Mnogokut.prikaz_info(self)                  # pozivanje druge klase


t1 = Trokut([2,3,4])                          # dodavanje stranica trokutu
t1.prikaz_info()                              # pozivanje prikaz_info
print('opseg je', t1.izracujan_opseg())       # u ckild klasi su dostupne sve metode iz parent klase

c1 = Cetverokut([2,3,4,5,])

'''fali dio'''
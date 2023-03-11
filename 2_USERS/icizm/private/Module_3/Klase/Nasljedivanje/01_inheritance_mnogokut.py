class Mnogokut:                                         # parent klasa 
    def __init__(self, stranica): 
        self.stranica = stranica

    def prikaz_info(self): 
        print('Mnogokut je 2D lik ravnih stranica')

    def izracunaj_opseg(self): 
        opseg = sum(self.stranica)
        return opseg
    

class Trokut(Mnogokut):                                   #child klasa 
    def prikaz_info(self): 
        print('Trokut je mnogokut s 3 kuta')
        Mnogokut.prikaz_info(self)
        #super().prikaz_info()                            #pozivanje iz gornje klase

class Cetverokut(Mnogokut): 
    def prikaz_info(self): 
        print('Trokut je mnogokut s 4 kuta')


t1 = Trokut([2, 3, 4])                          
t1.prikaz_info()
print('Opseg je', t1.izracunaj_opseg())                   #uchild klasi su dostupne sve metode iz parent klase


c1= Cetverokut([2,3,4,5])
c1.prikaz_info()


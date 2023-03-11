class Mnogokut:                 #parent class
    def __init__(self, stranice):
        self.stranice = stranice
    
    def prikaz_info(self):
        print('Mnogokut je 2D lik ravnih stanica')
    
    def izracunaj_opseg(self):
        opseg = sum(self.stranice)
        return opseg

class Trokut(Mnogokut):         #child class u zagradi od koga nasljeduje svojstva
    def prikaz_info(self):
        print('Trokut je mnogokut s 3 kuta')
        Mnogokut.prikaz_info(self)      #poziv preko imena ili super(). Bolje preko imena u slučaju da imamo više klasa
        super().prikaz_info()

class Cetverokut(Mnogokut):
    def prikaz_info(self):
        print('Četverokut je mnogokut s 4 kuta')


t1 = Trokut([2,3,4])
t1.prikaz_info()
print('Opseg je: ',t1.izracunaj_opseg())        #child klasi su dostupne sve metode parent klase

c1=Cetverokut([2,3,2,3])
c1.prikaz_info()
print('Opseg je: ', c1.izracunaj_opseg())
class Mnogokut:
    def __init__(self,stranice):
        self.stranice = stranice

    def prikaz_info(self):
        print ('Mnogokut je 2D lik ravnih stranica')

    def izračunaj_opseg(self):
        opseg = sum(self.stranice)
        return opseg

class Trokut (Mnogokut):
    def prikaz_info(self):
        print ('Trokut je mnogokut sa tri kuta')
        Mnogokut.prikaz_info(self) #1. način pozivanja iz glavne
        super().prikaz_info() #2. način pozivanja iz glavne

t1 = Trokut ([2,3,4,])

t1.prikaz_info()
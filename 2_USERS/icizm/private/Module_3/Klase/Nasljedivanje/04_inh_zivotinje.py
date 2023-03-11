class Zivotinja: 
    def __init__(self, broj_nogu, is_sisavac, is_ljubimac):  # ako želimo hardkodirati neku vrijendnost stavljamo je na kraj = fiksirati jednu vrijednost npr..., br_nogu = 0)
        self.broj_nogu = broj_nogu
        self.is_sisavac = is_sisavac  #is očekuje true ili false
        self.is_ljubimac = is_ljubimac

    def jede(self): 
        print('Jedem...')

class Pas(Zivotinja): 
    def __init__(self):
        super().__init__(4, True, True)

    def laje(self): 
        print('Lajem, jer sam pas...')

class Lav(Zivotinja): 
    def __init__(self):
        super().__init__(4, True, True)

    def rika(self): 
        print('Ričem jer sam lav...')

class Glista(Zivotinja): 
    def __init__(self):
        super().__init__(0, False, False)

    def gmize(self): 
        print('Gmižem jer sam glista...')

Garo = Pas()
Garo.jede()
Garo.laje()

Simba = Lav()
Simba.jede()
Simba.rika()

Marin = Glista()
Marin.jede()
Marin.gmize()
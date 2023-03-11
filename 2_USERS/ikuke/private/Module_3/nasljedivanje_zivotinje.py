

class Zivotinja:

    def __init__(self,vrsta,razred):
        self.vrsta = vrsta
        self.razred=razred
    
    def ispis(self):
        print(self.vrsta, self.razred)

   

class Pas(Zivotinja):
    pass

class Zec(Zivotinja):
    pass

class Glista(Zivotinja):
    pass


class Pas_ljubimac(Pas):
    def __init__(self, vrsta, razred, ime, godina):
        self.vrsta= vrsta
        self.razred=razred
        self.ime = ime
        self.godina=godina
        


ljubimac1 = Pas_ljubimac("canis","lupus","lija","2021")


ljubimac1.ispis()



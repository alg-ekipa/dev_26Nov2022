






class  Zivotinje:
    def __init__(self, br_nogu, is_sisavac, is_ljubimac):
        self.br_nogu = br_nogu 
        self.is_sisavac = is_sisavac  
        self.is_ljubimac = is_ljubimac  

    def jede(self):
        print('Jedem ...')

class Pas(Zivotinje):
    def __init__(self):
        super().__init__(4, True, True)

    def laje(self):
        print('Lajem, jer sam pase...')

class Lav(Zivotinje):
    def __init__(self):
        super().__init__(4, True, False)

    def rice(self):
        print('Ricem, jer sam lav...')


class Glsita(Zivotinje):
    def __init__(self):
        super().__init__(0, True, False)

    def gmiže(self):
        print('Gmižem, jer sam glista...')


Garo = Pas()
Garo.jede()
Garo.laje()
print()
King = Lav()
King.jede()
King.rice()
print()
Mrmi=Glsita()
Mrmi.jede()
Mrmi.gmiže()
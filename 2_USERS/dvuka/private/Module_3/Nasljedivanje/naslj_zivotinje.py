class Zivotinja:
    def __init__(self, br_nogu, is_sisavac, is_ljubimac):
        self.br_nogu=br_nogu
        self.is_sisavac=is_sisavac
        self.is_ljubimac=is_ljubimac

    def jede(self):
        print('Jedem.....')

class Pas(Zivotinja):
    def __init__(self):
        super().__init__(4,True,True)

    def laje(self):
        print('Lajem, jer sam pas...')

class Lav(Zivotinja):
    def __init__(self):
        super().__init__(4, True, False)

    def rice(self):
        print('Ričem, jer sam lav...')

class Glista(Zivotinja):
    def __init__(self):
        super().__init__(0,False,False)

    def gmize(self):
        print('Gmižem, jer sam glista...')

Garo=Pas()
Garo.jede()
Garo.laje()
print()
King=Lav()
King.jede()
King.rice()
print()
Mrmi=Glista()
Mrmi.jede()
Mrmi.gmize()
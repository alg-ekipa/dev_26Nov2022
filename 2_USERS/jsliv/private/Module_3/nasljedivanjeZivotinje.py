class Zivotinje:
    def __init__(self, broj_nogu, is_sisavac, is_ljubimac):
        self.broj_nogu = broj_nogu
        self.is_sisavac = is_sisavac
        self.is_ljubimac = is_ljubimac
    
    def jede(self):
        print("Jedem...")
    
class Pas(Zivotinje):
    def __init__(self):
        super().__init__(4, True, True)

    def laje(self):
        print("Lajem jer sam pas...")

class Lav(Zivotinje):
    def __init__(self):
        super().__init__(4, True, False)

    def rice(self):
        print("Ricem jer sma lav...")

class Glista(Zivotinje):
    def __init__(self):
        super().__init__(0, False, False)

    def gmize(self):
        print("Gmizem jer sam glista...")

Garo = Pas()
Garo.jede()
Garo.laje()
print()

King = Lav()
King.jede()
King.rice()
print()

Mrmi = Glista()
Mrmi.jede()
Mrmi.gmize()
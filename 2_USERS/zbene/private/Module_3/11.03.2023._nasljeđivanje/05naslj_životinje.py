class Životinja:
    def __init__(self, broj_nogu, is_sisavac, is_ljubimac):
        self.broj_nogu = broj_nogu
        self.is_sisavac = is_sisavac
        self.is_ljubimac = is_ljubimac

    def jede (self):
        print ('Jedem...')
    
class Pas (Životinja):
    def __init__ (self):
        super().__init__(4, True, True)
    
    def laje (self):
        print ('Lajem jer sam pas...')

class Lav (Životinja):
    def __init__(self):
        super().__init__(4, True, False)
    
    def riče (self):
        print ('Ričem jer sam lav...')

class Glist (Životinja):
    def __init__(self):
        super().__init__(0, False, True)
    
    def gmiže(self):
        print ('Gmižem jer sam glista...')

Garo = Pas ()
Garo.jede()
Garo.laje()

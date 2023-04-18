#preporuka naziv klase velikim slovom bez odvajanja
# općenito


class NazivKlase:
    """docstring"""
    pass

objekt1= NazivKlase()
objekt2= NazivKlase()


class TV_aparati():
    #konstruktor je metoda koja se zove __init__(initializacija)

    def __init__(self,model,proizvodac, dijagonala, ukljucen=False, program=0,glasnoca=0):
        self.model = model
        self.proizvodac=proizvodac
        self.dijagonala=dijagonala
        self.ukljucen=ukljucen
        self.program=program
        self.glasnoca=glasnoca


    def ispis(self):
        print('proba')
        print(self.model, self.proizvodac, self.dijagonala, self.ukljucen, self.ukljucen, self.glasnoca)

    def ukljuci(self):
        self.ukljucen=True
        self.glasnoca=8
        self.program=1


   
def input_TV():
    model=input('unesi model:')
    proizvodac=input('unesi proizvodaca:')
    dijagonala=input('unesi dijagonalu:')
    return TV_aparati(model,proizvodac,dijagonala)




televizor1=input_TV()
televizor2=input_TV()

print (televizor1.proizvodac)
print (televizor2.proizvodac)
print (televizor2.ukljucen)
televizor2.ukljuci()
print (televizor2.ukljucen)

televizor1.ispis()
televizor2.ispis()

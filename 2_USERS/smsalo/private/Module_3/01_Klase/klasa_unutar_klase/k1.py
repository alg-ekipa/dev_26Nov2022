class Vanjska:
    def __init__(self):
        print('Pozvan konstuktor vanjske klase')
    
    def ispis(self):
        print('Funkcija ispisa')

    class Unutarnja:
        def __init__(self):
            print('Pozvan konstruktor unutarnje klase')
        def prikazuje(self):
            print('Funkcija prikaza')

objekt=Vanjska()
objekt_unutar=objekt.Unutarnja()

objekt_unutar.prikazuje()
objekt.Unutarnja().prikazuje()   #funkcija prikazuje ne radi na vanjskom ukoliko ju ne definiramo kao .Unutarnja().



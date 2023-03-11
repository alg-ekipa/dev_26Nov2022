class Vanjska:
    def __init__(self):
        print ('Pozvan konstruktor vanjske klase')
        print ('--------------------------------')

    def ispisi(self):
        print('Funkcija ispisa')

    class Unutarnja:
        def __init__(self):
            print ('Pozvan konstruktor unutarnje klase')
            print()

        def prikazi(self):
            print ('Funkcija prikaza')
            print ('----------------')



objekt = Vanjska ()
objekt_unutar= objekt.Unutarnja()

objekt_unutar.prikazi()
objekt.Unutarnja().prikazi()

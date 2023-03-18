class Vanjska:
    def __init__(self):
        print('Pozvan konstruktor vanjske klase')

    def ispis(self):
        print('Funkcija ispisa')

    class Unutarnja:
        def __init__(self):
            print('Pozvan konstruktor unutarnje klase')
        def prikazi(self):
            print('Funkcija prikaza')

objekt=Vanjska()
objekt_unutar=objekt.Unutarnja()

#objekt.rikazi()  -objekt je klase vanjska i ne moe direktn na ovaj način prisupiti metodi unutara klase unutarnja

objekt_unutar.prikazi()
objekt.Unutarnja().prikazi()
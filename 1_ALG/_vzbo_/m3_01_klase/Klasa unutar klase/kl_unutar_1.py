class Vanjska:
    def __init__(self):
        print('Pozvan konstruktor vanjske klase')

    def ispisi(self):
        print('Funkcija ispisa')

    class Unutarnja:
        def __init__(self):
            print('Pozvan konstruktor unutarnje klase')
        def prikazi(self):
            print('Funkcija prikaza')

objekt = Vanjska()
objekt_unutar = objekt.Unutarnja()

#objekt = objekt_unutar -- ako želimo da nam se isto zove onda objektu objekt pridružimo novu vrijednost (objekt_unutar)

#objekt.prikazi()   #--objekt je klase Vanjska i ne može direkno na ovaj način pristupiti metodi unutar klase Unutarja 

objekt_unutar.prikazi()
objekt.Unutarnja().prikazi()
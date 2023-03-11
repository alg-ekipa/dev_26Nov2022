class Vanjska:
    def __init__(self):
        print('Pozvan konstruktor vanjeske klase')

    def ispis(self): 
        print('Funkcija ispisa')

    class Unutarnja: 
        def __init__(self):
            print('Pozvan konstruktor unutarnje klase')

        def prikazi(self): 
            print('Funkcija prikaza')

objekt = Vanjska()
objekt_unutar = objekt.Unutarnja()

objekt_unutar.prikazi()
# objekt = objekt_unutar -ako želimo da nam se isto zove onda objektu objekt pridružimo novu vrijednost (objekt_unutar)
# objekt.prikazi() - objekt je klase Vanjska i ne može direktno na ovaj način pristupiti metodi unutar klase Unutarnja (ne vidi ga)

objekt.Unutarnja().prikazi()

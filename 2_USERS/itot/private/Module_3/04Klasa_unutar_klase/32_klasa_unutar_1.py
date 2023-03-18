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

objekt = Vanjska()
objekt_unutar = objekt.Unutarnja()

#objekt = objekt_unutar     -- ako želimo da nam se isto zove onda objektu pridružimo ovu vrijednost (objekt_unutar)

# objekt.prikazi() - objekt je klase Vanjska i ne može direktno na ovaj način pristupiti metodi unutar klase Unutarnja

objekt_unutar.prikazi()
objekt.Unutarnja().prikazi()
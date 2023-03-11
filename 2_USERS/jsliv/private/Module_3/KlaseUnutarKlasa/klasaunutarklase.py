class Vanjska:
    def __init__(self):
        print("Pozvan konstrukotr vanjske klase.")
    
    def ispis(self):
        print("Funkcija ispisa.")

    class Unutarnja:
        def __init__(self):
            print("Pozvan konstruktor unutarnje klase.")
        def prikaz(self):
            print("Funkcija prikaza.")

objekt = Vanjska()
objekt_unutar =   objekt.Unutarnja()

objekt_unutar.prikaz()
objekt.Unutarnja().prikaz()
class Student:
    def __init__(self, ime, mbr):
        print ('Pozvan konstruktor vanjske klase')
        print ('--------------------------------')
        self.ime=ime
        self.mbr=mbr
        self.lap=self.Laptop() #varijablu za laptop definiramo sa self, ona je klasa unutar ove klase Student


    def prikazi(self):
        print('Funkcija ispisa')
        print (self.ime, self.mbr)

    class Laptop:  #svaki student ima laptop sa svojstvima i metodama koje onda definiramo u novoj klasi
        def __init__(self):
            print ('Pozvan konstruktor unutarnje klase')
            self.marka='HP'
            self.procesor='i5'
            self.ram=8

        def ispis(self):   
            print(self.marka, self.procesor, self.ram)

        def prikazi(self):
            print ('Funkcija prikaza')
            print ('----------------')





objekt = Student()


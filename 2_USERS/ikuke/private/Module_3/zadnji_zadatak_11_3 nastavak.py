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
            print ('Pozvan konstruktor unutarnje klase')  #u ovom primjeru svi studenti imaju ista svojstva
            self.marka='HP'
            self.procesor='i5'
            self.ram=8

        def ispis(self):   
            print(self.marka, self.procesor, self.ram)

        def prikazi(self):
            print ('Funkcija prikaza')
            print ('----------------')





s1 = Student('Ivana Ivanović', 2455)
objekt2= Student('Marko Marković', 5580)

lap1= s1.lap
print (lap1)
lap1.ispis()


lap1 = Student.Laptop()
lap1.ispis()
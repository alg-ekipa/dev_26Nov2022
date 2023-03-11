class Student:
    def __init__(self, ime, mbr, dan, mjesec, godina):
        print ('Pozvan konstruktor vanjske klase')
        print ('--------------------------------')
        self.ime=ime
        self.mbr=mbr
       # self.lap=self.Laptop() #varijablu za laptop definiramo sa self, ona je klasa unutar ove klase Student
        self.datum_rodj = self.Datum_rodjenja(dan, mjesec, godina)


    def prikazi(self):
        print('Funkcija ispisa')
        print ('Ime:', self.ime, 'Prezime:', self.mbr)



    class Datum_rodjenja:
        def __init__(self, dan, mjesec, godina):
            self.dan=dan
            self.mjesec=mjesec
            self.godina=godina

        def ispis(self):
            print('Funkcija ispisa datuma rođenja')
            print ('Datum rođenja:', self.dan, self.mjesec, self.godina)

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


s1 = Student('Ivana Ivanović', 2455, 6, 11, 1981)
objekt2= Student('Marko Marković', 5580, 2, 2, 2012)


s1.prikazi()

#paziti da se funkcija poziva nad objektom
objekt2.datum_rodj.ispis()

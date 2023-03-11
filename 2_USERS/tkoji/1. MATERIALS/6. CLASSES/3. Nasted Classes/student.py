class Student:
    def __init__(self, ime, mbr, marka, cpu, ram):
        self.ime = ime
        self.mbr = mbr
        self.lap = self.Laptop(marka, cpu, ram)  # varijablu za laptop definiramo sa self, ona je zapravo klasa unutar ove klase Student

    def prikazi(self):
        print(self.ime, self.mbr)
        self.lap.ispis()

    class Laptop:           # svaki student ima laptop, sa svojstvima i metodama, koje onda definiramo u novoj klasi
        def __init__(self, marka, cpu, ram):     # u ovom primjeru svi laptopi imaju ista svojstva
            self.marka = marka
            self.cpu = cpu
            self.ram = ram

        def ispis(self):
            print(self.marka, self.cpu, self.ram)

s1 = Student('Ivana Ivanović', 2455, 'HP', 'i5', 16)
s2 = Student('Marko Marković', 8843, "Lenovo", 'i7', 24)

s1.prikazi()
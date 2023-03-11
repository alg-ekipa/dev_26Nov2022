class Student:
    def __init__(self, ime, mbr, marka, cpu, ram): 
        self.ime = ime
        self.mbr = mbr
        self.laptopi = self.Laptop(marka, cpu, ram)      # Varijablu za laptop definiramo sa self, ona je k in k Student 

    def prikazi(self): 
        print(self.ime, self.mbr)
        self.laptopi.ispis()

    class Laptop:                # Svaki student ima laptop sa svojstvima i metodama, koje onda definiramo u novoj klasi
        def __init__(self, marka, cpu, ram):      # u ovom primjeru svi laptopi imaju ista svojstva
            self.marka = marka
            self.cpu = cpu
            self.ram = ram

        def ispis(self): 
            print('Student posjeduje laptop:', self.marka, self.cpu, self.ram)

s1 = Student('Ivica Ivošević', 868686, 'HP', 'i7', 43)
s1.prikazi()
s2 = Student('Mirjan Markovec', 98569854, 'Lenovo', 'nj3', 34)
s2.prikazi()


class Student:
    def __init__(self, ime, mbr): 
        self.ime = ime
        self.mbr = mbr
        self.lap = self.Laptop()      # Varijablu za laptop definiramo sa self, ona je k in k Student 

    def prikazi(self): 
        print(self.ime, self.mbr)

    class Laptop:                # Svaki student ima laptop sa svojstvima i metodama, koje onda definiramo u novoj klasi
        def __init__(self):      # u ovom primjeru svi laptopi imaju ista svojstva
            self.marka = 'HP'
            self.cpu = 'i5'
            self.ram = 8
        def ispis(self): 
            print(self.marka, self.cpu, self.ram)

s1 = Student('Ivica Ivošević', 868686)
s2 = Student('Mirjan Markovec', 98569854)

# lap1 = s1.lap
# print(lap1) - ispisao da je to objekt ružno

lap1 = Student.Laptop()
lap1.ispis()
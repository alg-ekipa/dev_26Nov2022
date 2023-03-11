class Student:
    def __init__(self, ime, oib):
        self.ime = ime
        self.oib = oib
        self.lap = self.Laptop()   #varijablu dfiniramo sa self, ona je zapravo klasa unutar klase Student

    def prikazi(self):
        print(self.ime, self.oib)
    
    class Laptop:    #svaki student im asvoj laptop sa svojstvima i metodama, koja onda definiramo u novoj klasi
        def __init__(self,):   #u ovom primjeru svi laptopi imaju ista svojstva
            self.marka = "HP"
            self.cpu = "i5"
            self.ram = 8
        
        def ispis(self):
            print(self.marka, self.cpu, self.ram)

s1 = Student("Luka Lukić", 12345)
s2 = Student("Marko Marković", 88835)

lap1 = s1.lap
#print(lap1)


lap1 = Student.Laptop()
lap1.ispis()

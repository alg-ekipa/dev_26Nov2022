class Student:
    def __init__ (self, ime, MB):
        self.ime = ime
        self.MB = MB
        self.lap = self.Laptop #barijablu za laptop definiramo sa self, ona je zapravo klasa unutar ove klase Student

    def prikaži (self):
        print (self.ime, self.MB)

    class Laptop:   #svaki student ima laptop sa svojstvima i metodama, kojeg onda definiramo u novoj klasi
        def __init__ (self): #u ovom primjeru svi laptopi imaju ista svojstva
            self.marka = 'HP'
            self.CPU = 'i5'
            self.RAM = 8
        
        def ispis (self):
            print (self.marka, self.CPU, self.RAM)

s1 = Student ('Ivana Ivanović', 2455)
s2 = Student ('Marko Marković', 8843)

#lap1 = s1.lap
#print (lap1)

lap1 = Student.Laptop()
lap1.ispis()
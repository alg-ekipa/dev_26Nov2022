class Student:
    def __init__(self, ime,mbr):
        self.ime=ime
        self.mbr=mbr
        self.lap=self.Laptop()  #varijablu za laptotp definiramo sa self, ona je zapravo klasa unutar ove klase Student

    def prikazi(self):
        print(self.ime, self.mbr)

    class Laptop:           #svaki student ima laptop, sa svojstvima i metodama koje onda definiramo u novoj klasi
        def __init__(self): #u ovom primjeru svi laptopi imaju ista svojstva
            self.marka='HP'
            self.cpu='i5'
            self.ram=8
        def ispis(self):
            print(self.marka, self.cpu, self.ram)

s1=Student('Ivana Ivanović', 2455)
s2=Student('Marko Marković', 8843)

#lap1=s1.lap
#print(lap1)


lap1=Student.Laptop()
lap1.ispis()

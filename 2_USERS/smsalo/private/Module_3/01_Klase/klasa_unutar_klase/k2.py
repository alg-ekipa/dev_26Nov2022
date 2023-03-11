class Student:
    def __init__(self, ime, MB):
        self.ime=ime
        self.MB=MB
        self.lap=self.Laptop()      #varijablu za laptop definiramo sa self, ona je zaprvo klasa unutar ove klase
    
    def ispis(self):
        print(f'Ime: {self.ime}, MB: {self.MB}')
    
    class Laptop:               #svaki student ima laptop sa svojstvima i metodama
        def __init__(self):
            self.marka='HP'
            self.cpu='i5'
            self.ram=8
        def ispis(self):
            print(self.marka, self.cpu, self.ram)

s1=Student('Ivana Iva', '12346')
s2=Student('Marko Markic', '3245668')

s1.ispis()
lap1=s1.lap
lap1.ispis()

lap1=Student.Laptop()
lap1.ispis()
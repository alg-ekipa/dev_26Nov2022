class Student:
    def __init__ (self, ime, MB, dan, mjesec, godina, marka, CPU, RAM):
        self.ime = ime
        self.MB = MB
        self.dat_rođ = self.Datum_rođenja(dan, mjesec, godina)
        self.lap = self.Laptop(marka, CPU, RAM)
    
    def ispiši (self):
        print (f'Ime: {self.ime}, MB: {self.MB}')
        self.dat_rođ.prikaži()

    class Datum_rođenja:
        def __init__ (self, dan, mjesec, godina):
            self.dan = dan
            self.mjesec = mjesec
            self.godina = godina
   
        def prikaži (self):
            print (f'Datum rođenja: {self.dan}.{self.mjesec}.{self.godina}.')

    class Laptop:
        def __init__ (self, marka, CPU, RAM):
            self.marka = marka
            self.CPU = CPU
            self.RAM = RAM
    
        def ispis (self):
            print (self.marka, self.CPU, self.RAM)

s1 = Student ('Krešo', 3144, 10, 12, 2000, 'Lenovo', 'i9', 16)
s1.ispiši() ##################
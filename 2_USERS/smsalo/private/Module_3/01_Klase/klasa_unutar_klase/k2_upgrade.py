class Student:
    def __init__(self, ime, MB, marka, cpu, ram):
        self.ime=ime
        self.MB=MB
        self.lap=self.Laptop(marka, cpu, ram)  
    
    def ispis(self):
        print(f'Ime: {self.ime}, MB: {self.MB}')
        self.lap.ispis_lap()
    
    class Laptop:              
        def __init__(self, marka, cpu, ram):
            self.marka=marka
            self.cpu=cpu
            self.ram=ram
        def ispis_lap(self):
            print(self.marka, self.cpu, self.ram)

s1=Student('Ivana Iva', '12346','HP', 'ii', 12)
s1.ispis()

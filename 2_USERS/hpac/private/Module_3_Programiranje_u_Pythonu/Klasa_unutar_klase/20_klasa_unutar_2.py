class Student:
    def __init__(self, ime, mbr):
        self.ime = ime
        self.mbr = mbr
        self.lap = self.Laptop()    # varijablu za laptop definiramo sa self, ona je zapravo klasa unutar ove klase Student

    def ispisi(self):
        print(self.ime, self.mbr)

    class Laptop:   # Svaki student ima laptop, sa svojstvima i metodama, koje onda definiramo u novoj klasi
        def __init__(self):
            self.marka = 'HP'
            self.cpu = 'i5'
            self.ram = 8
        def ispis (self):
            print(self.marka, self.cpu, self.ram)   

s1 = Student('Marko', 12345)
s2 = Student('Krešo', 74123)

lap1 = s1.lap
print(lap1)     # ispisuje u čudnom obliku, tj  vidimo da se objekt nalazi negdje
lap1.ispis()    # uredan ispis laptopa

lap1 = Student.Laptop()
lap1.ispis()
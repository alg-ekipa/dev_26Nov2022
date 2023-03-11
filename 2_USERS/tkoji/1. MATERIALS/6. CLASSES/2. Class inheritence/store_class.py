# Izraditi klasu Proizvod te tri klase STOL, SVJETILJKA, TEPIH koje nasljeduju klasu Proizvod
# svojstva: sifra, cijena, raspolozivost, boja, dimenzije, materijal, oblik, zarulja...
# iskoristi pripremljeni rjecnik

# Od pripremljenih rjecnika s podacima izradite objekte za sve elemente

# napisi metodu za pronalazak i ispis
# Ispisi svjetiljke sa zaruljom
# Ispisi Drvene stolove
# Ispisi okrugle tepihe
# Proizvode sa cijenom ispod 1000kn     
# Raspolozive proizvode    
# Ukupnu cijenu svih svjetiljki   

stolovi_rjecnik = {
    '0186': ['stol Jack', 700.00, True, 'smeđa', 'drvo', 4],
    '0203': ['stol Kathy', 880.00, True, 'smeđa', 'staklo', 3],
    '1234': ['stol Tomy', 1250.00, True, 'bijela', 'staklo', 4],
    '4002': ['stol Ohm', 940.00, True, 'crna', 'metal', 1],
    '0923': ['stol Heda', 940.00, False, 'crna', 'drvo', 1],
    '1773': ['stol Lucas', 940.00, True, 'crna', 'drvo', 4]
}

svjetiljka_rjecnik = {
    '0001': ['svjetiljka Zadar', 1200.00, True, 'zlatna', 'zlato', 'zarulja'],
    '0002': ['svjetiljka Zagreb', 2800.00, True, 'plava', 'staklo', 'zarulja'],
    '0003': ['svjetiljka Dubrava', 800.00, False, 'zelena', 'srebro', 'bez'],
    '0004': ['svjetiljka Rijeka', 400.00, False, 'roza', 'zlato', 'bez'],
    '0005': ['svjetiljka Dubrovnik', 5400.00, True, 'magenta', 'platina', 'zarulja'],
    '0006': ['svjetiljka Madrid', 55950.00, True, 'crvena', 'platina', 'bez']
}

tepisi_rjecnik = {
    '0007': ['tepih Melita', 8000.00, True, 'zlatna', 'pamuk', 'okrugao'],
    '0008': ['tepih Lana', 7200.00, True, 'plava', 'svila', 'pravokutni'],
    '0009': ['tepih Sanja', 480.00, False, 'zelena', 'pamuk', 'okrugao'],
    '0010': ['tepih Emina', 525.00, False, 'roza', 'plastika', 'pravokutni'],
    '0011': ['tepih Laura', 320.00, True, 'magenta', 'plastika', 'okrugao'],
    '0012': ['tepih Tea', 12524.00, True, 'crvena', 'svila', 'pravokutni']
}


class Store:
    def __init__(self, name, price, available, color, material):
        self.id = id
        self.name = name
        self.price = price
        self.available = available
        self.color = color
        self.material = material

    def calculate_price(self):
        if self.price <= 1000:
            print(f'{self.name}')
        
    def availablity(self):
        if self.available == True:
            print(f'{self.name}')

class Table(Store):
    def __init__(self, name, price, available, color, material, legs):
        super().__init__(name, price, available, color, material)
        self.legs = legs

    def table_print(self):
        print(f'''
        Name: {self.name}
        Color: {self.color}
        Material: {self.material}
        Number of legs: {self.legs}
        Price: {self.price} HRK.''')

class Lamp(Store):
    def __init__(self, name, price, available, color, material, bulb):
          super().__init__(name, price, available, color, material)
          self.lamp = bulb

class Carpet(Store):
        def __init__(self, name, price, available, color, material, shape):
            super().__init__(name, price, available, color, material) 
            self.shape = shape


table_object_list = list()
lamp_object_list = list()
carpet_object_list = list()

# Tables 
for table in stolovi_rjecnik.values():
    table_name = table[0]
    table_price = table[1]
    table_availability = table[2]
    table_color = table[3]
    table_material = table[4]
    table_legs = table[5]
    
    table_object = Table(table_name, table_price, table_availability, table_color, table_material, table_legs)
    table_object_list.append(table_object)


print("Tables: ")
for table_object in table_object_list:
    table_object.table_print()

print("\nTable prices less than 1k HRK: ")
for table_object_prices in table_object_list:
    table_object_prices.calculate_price()

print("\nTables currently available: ")
for table_object_avail in table_object_list:
    table_object_avail.availablity()

#

for lamp in stolovi_rjecnik.values():
    lamp_name = lamp[0]
    lamp_price = lamp[1]
    lamp_availability = lamp[2]
    lamp_color = lamp[3]
    lamp_material = lamp[4]
    lamp_included = lamp[5]

    table_object = Lamp(lamp_name, lamp_price, lamp_availability, lamp_color, lamp_color, lamp_included)
    table_object_list.append(table_object)

    

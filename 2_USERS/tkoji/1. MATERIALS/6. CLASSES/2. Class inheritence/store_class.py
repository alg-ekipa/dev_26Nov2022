# Izraditi klasu Proizvod te tri klase STOL, SVJETILJKA, koje nasljeduju klasu Proizvod
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

      
    

# class Lamp(Store):
#     def __init__(self, name, price, available, color, material, bulb):
#           super().__init__(name, price, available, color, material)
#           self.bulb = bulb
          
#     def lamps_bulb(self):
#         if self.bulb == 'zarulja':
#             print("This lamp comes with a bulb.")

# class Carpet(Store):
#         def __init__(self, name, price, available, color, material, shape):
#             super().__init__(name, price, available, color, material) 
#             self.shape = shape





stolovi_rjecnik = {
    '0186': ['Jack', 700.00, True, 'smeđa', 'drvo', 4],
    '0203': ['Kathy', 880.00, True, 'smeđa', 'staklo', 3],
    '1234': ['Tomy', 1250.00, True, 'bijela', 'staklo', 4],
    '4002': ['Ohm', 940.00, True, 'crna', 'metal', 1],
    '0923': ['Heda', 940.00, False, 'crna', 'drvo', 1],
    '1773': ['Lucas', 940.00, True, 'crna', 'drvo', 4]
}

class Store:
    def __init__(self, name, price, available, color, material):
        self.id = id
        self.name = name
        self.price = price
        self.available = available
        self.color = color
        self.material = material

    def is_affordable(self):
        if self.price <= 1000:
            print(f'{self.name}', end=' ')
        
    def is_available(self):
        if self.available == True:
            print(f'{self.name}', end=' ')

class Table(Store):
    def __init__(self, name, price, available, color, material, legs):
        super().__init__(name, price, available, color, material)
        self.legs = legs

    def get_wood_table(self):
        if self.material == 'drvo':
            print(f'Wooden tables are: {self.name}.')

    def __str__(self):
        print(f'''
        Name: {self.name}
        Color: {self.color}
        Material: {self.material}
        Number of legs: {self.legs}
        Price: {self.price} HRK.''')


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
    table_object.__str__()

print("\nTable prices less than 1k HRK: ")
for table_object_prices in table_object_list:
    table_object_prices.is_affordable()

print("\n\nTables currently available: ")
for table_object_avail in table_object_list:
    table_object_avail.is_available()
    
print("\nWooden tables ")
for table_object_wood in table_object_list:
    table_object_wood.get_wood_table()
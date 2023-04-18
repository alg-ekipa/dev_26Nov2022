from datetime import datetime as dt

class Invoice:
    def __init__(self, number, date, items):
        self.number = number
        self.date = date
        self.items = items
        self.pdv = 0.25
        self.total = 0
    
    def __str__(self):
        print("Ovo je ispis racun u klasi Invoice.")
        
    def calculate_sum(self):
        print(type(self.items))
        for price in self.items.values():
            print(f'List of prices {price}')
            self.total = self.total + price
            return self.total
    
class InvoiceGenerator(Invoice):
    def __init__(self,  number, date, items, seller, oib):
        super().__init__(number, date, items)
        self.seller = seller
        self.oib = oib

    def __str__(self):
        print("________" + self.number  + "________")
        print("________" + self.seller  + "________")
        print("________" + self.oib  + "________")
        print(f'________ {self.date}  ________')
    
    
    def calculate_sum(self):
        print(type(self.items))
        for price in self.items.values():
            print(f'List of prices {price}')
            self.total = self.total + price
            return self.total
       
## MAIN PROGRAM  
invoice_database = list()
invoice_counter = 1

def generate_invoice(counter):
    invoice_items = dict()
    invoice_number = f'R-{counter}-2023'
    date = dt.now()
    seller = 'Konzum'
    oib = '123456'
    
    while True:
        input_item = input("Add an item: ")
        input_price = float(input("Add a price: "))
        invoice_items[input_item] = input_price
        
        if not input("Do you wish to add more item? No to quit. "):
            break

    invoice_object = Invoice(invoice_number, date, invoice_items) #, seller, oib)
    return invoice_object

while True:
    invoice = generate_invoice(invoice_counter)
    invoice_counter += 1

    invoice_database.append(invoice)
    print(invoice_database)
    
    if not input('Unosimo novi račun? (NE - Enter) '):
        break

    
for a in invoice_database:
    print(a.__str__())
    
for b in invoice_database:
    print(b.calculate_sum())
    
    
    
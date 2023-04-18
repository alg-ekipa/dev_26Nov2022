from datetime import datetime as dt

class InvoiceItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.name} - {self.price:.2f} kn"
    

class Invoice:
    def __init__(self, number, date, items, pdv=0.25):
        self.number = number
        self.date = date
        self.items = items
        self.pdv = pdv
        
    def add_item(self, name, price):
        item = InvoiceItem(name, price)
        self.items.append(item)
        
    def invoice_header(self, seller, oib, location_id, cashier):
        self.seller = seller
        self.oib = oib
        self.location_id = location_id
        self.cashier = cashier
    
    def __str__(self):
        item_list = "\n".join([str(item) for item in self.items])
        total = sum([item.price for item in self.items])
        pdv = total * self.pdv
        grand_total = total + pdv
        date_string = self.date.strftime("%d.%m.%Y")
        
        return f"{'='*30}\n" \
               f"{'RAČUN':^30}\n" \
               f"{'='*30}\n" \
               f"{'Broj računa:':<15} {self.number:>15}\n" \
               f"{'Datum izdavanja:':<15} {date_string:>15}\n" \
               f"{'Prodavač:':<15} {self.seller:>15}\n" \
               f"{'OIB:':<15} {self.oib:>15}\n" \
               f"{'Lokacija:':<15} {self.location_id:>15}\n" \
               f"{'Blagajnik:':<15} {self.cashier:>15}\n" \
               f"{'='*30}\n" \
               f"{item_list}\n" \
               f"{'-'*30}\n" \
               f"{'Ukupno:':<25} {total:>5.2f} kn\n" \
               f"{'PDV (25%):':<25} {pdv:>5.2f} kn\n" \
               f"{'='*30}\n" \
               f"{'UKUPNO ZA NAPLATU:':<25} {grand_total:>5.2f} kn\n" \
               f"{'='*30}\n"


class InvoiceGenerator:
    def __init__(self, number, date, reference, counter):
        self.number = number
        self.date = date
        self.refernce = reference
        self.counter = counter
        
        
class InvoiceMath:
    def __init__(self, price, pdv=0.25):
        self.price = price
        self.pdv = pdv
        
    def calculate_total(self):
        total = 0
        grand_total = total + self.price
        return grand_total



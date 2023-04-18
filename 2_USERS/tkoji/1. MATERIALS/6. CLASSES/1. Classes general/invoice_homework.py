#TODO 
# - generate dictionary of items to avoid manual input
# - for each item add category (food, beverages, housing, tools etc.) and add as a flag to each itme
# - in the end of an invoice calculate the percentage per category
# - generate the invoice to file
# - how to handle multiple clinets (Konzum, Plodine, Spar)? - class Customer() ???


from datetime import datetime as dt

class InvoiceName():
    def __init__(self, name, pdv=0.25):
        self.name = name
        self.pdv = pdv
        
class Invoice(InvoiceName)
    def __init__ (self, number, date, items):
        self.number = number
        self.date = date
        self.items = items
        
    def add_item(self, item, price):
        self.item = item
        self.price = price
    
    def calculate_sum(self):
        item_list = []
        total = sum(self.inv_items.values())
        return int(total)
    
    
    def calculate_pdv(self):
        sum_pdv = self.calculate_sum() * self.pdv
        sum_pdv_total = self.calculate_sum() + sum_pdv
        return sum_pdv_total
    
    def __str__(self):
        print(f'\n************ {self.company}  ************')
        print(f'Invoice number:\t{self.inv_num}')
        print(f'Invoice date:\t{self.date}')
        print("*" * 44)
        for item,price in self.inv_items.items():
            print(f'{item}\t\t{price}')
        print("_" * 44) 
        print(f'Total: \t\t\t\t{float(self.calculate_sum())} EUR.')
        print(f'Total + PDV:\t\t\t{self.calculate_pdv()} EUR.')   

            
def generate_invoice(counter):
    single_invoice = dict()
    invoice_number = f'R-{counter}-2023'
    invoice_date = dt.now().isoformat(' ', 'seconds')
    
    while True:
        item_name = input("Input item_name: ")
        item_price = float(input("Input item price: "))
        single_invoice[item_name] = item_price
        if not input("Input yes to add more articles or ENTER to quit."):
            break
        
    invoice_object = Invoice(inv_company,counter,single_invoice,invoice_date)
    return invoice_object

inv_ledger = list()
inv_counter = 1
inv_company = 'Konzum d.d - P001'

while True:
    new_invoice = generate_invoice(inv_counter)
    inv_counter += inv_counter
        
    inv_ledger.append(new_invoice)  
    if not input("Input yes if you wish to shop more or hit ENTER to quit."):
        break

for new_invoice in inv_ledger:
    new_invoice.print_invoice()



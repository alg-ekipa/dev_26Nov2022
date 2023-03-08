
from datetime import datetime as dt

class Invoice():
    def __init__(self, company, inv_num, inv_items, date, pdv=0.25):
        self.company = company
        self.inv_num = inv_num
        self.inv_items = inv_items
        self.date = date
        self.pdv = pdv
        self.total = 0
        
    def calculate_sum(self):
        total = sum(inv_items.values())
        return int(total)
    
    def calculate_pdv(self):
        sum_pdv = self.calculate_sum() * self.pdv
        sum_pdv_total = self.calculate_sum() + sum_pdv
        print(f'Total with pdv: {sum_pdv_total}')
        return sum_pdv_total
    
    def print_invoice(self):
        print(f'\n************ {self.company}  ************')
        print(f'Invoice number:\t{self.inv_num}')
        print(f'Invoice date:\t{self.date}')
        print("*" * 44)
        for item,price in self.inv_items.items():
            print(f'{item}\t\t{price}')
              
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

#TODO 
# - formating ispisa
# - split price and pdv
# - print grand total 

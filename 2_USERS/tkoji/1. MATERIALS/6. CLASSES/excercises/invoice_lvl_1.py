
#variables
invoice_number = 'R1-2023-01'
invoice_date = '4th Mar 2023'
invoice_items = {
    'laptop': 12000,
    'montor': 1250,
    'mouse' : 70,
    'keyboard': 150
} 

price_total = 0
price_vat = 0.25

for price in invoice_items.values():
    price_total = price_total + price
    
price_vat = price_total * (1+price_vat)

print(invoice_number)
print(invoice_date)
print(invoice_number)
print("*"*20) 
for good,price in invoice_items.items():
    print(f'{good} costs: {price}')
print("-"*20)    
print(f'TOTAL:\t{price_total}')
print(f'TOTAL + VAT:\t{price_vat}')

class Invoice():
    pass
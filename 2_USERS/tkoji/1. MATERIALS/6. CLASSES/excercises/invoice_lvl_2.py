def invoice_create(counter, vat, date):
    
    invoice_items =  {}
    
    while True:
        invoice_item = input("Plese enter the item: ")
        invoice_price = float(input("Please enter the price: "))
        invoice_items[invoice_item] = [invoice_price]
        if not input('Add more or hit Enter to exist: '):
            break
        
invoice_counter = 1
invoice_vat = 0.25
invoice_date = '04th Feb 2023'

invoice_list = []

while True:
    create_new_invoice = invoice_create(invoice_counter,invoice_vat,invoice_date)
    invoice_counter += 1
    invoice_number = f'R-{invoice_counter}-2023'
    invoice_list [invoice_counter] = create_new_invoice
    
    if not input("Do you wish to create a new invoice? Enter if not. "):
        break
    
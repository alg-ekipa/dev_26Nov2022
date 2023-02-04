
import datetime as dt
from time import sleep

def generate_invoice(invoice):
    time_now = dt.datetime.now()
    seconds = time_now.second
    minute = time_now.minute
    hour = time_now.hour
    day = time_now.day
    month = time_now.month
    year = time_now.year
    
  
    account_id =  f'{day}.{month}.{year}.\t {hour}:{minute}:{seconds}\t Broj racuna: {invoice_number}.'
    return account_id

invoice_number =  1
for i in range(5):
    invoice_number =  i+1
    sleep(2)
    print(generate_invoice(invoice_number))



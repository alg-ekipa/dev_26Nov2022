import datetime as dt
from time import sleep

def generiraj_racun(broj_racuna):

    sadasnji_trenutak=dt.datetime.now()

    day=sadasnji_trenutak.day
    month=sadasnji_trenutak.month
    year=sadasnji_trenutak.year

    sat=sadasnji_trenutak.hour
    minuta=sadasnji_trenutak.minute
    sekunda=sadasnji_trenutak.second


    account_id=f'{day}. {month}. {year}.\t{sat}:{minuta}:{sekunda}\nBroj računa: {broj_racuna}'
    return account_id

for i in range(5):
    broj_rac=i+1
    sleep(1)
    print(generiraj_racun(broj_rac))

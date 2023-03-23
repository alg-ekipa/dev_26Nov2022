import datetime as dt
from time import sleep

def generiraj_račun(broj_racuna):

    sadasnji_trenutak = dt.datetime.now()

    dan = sadasnji_trenutak.day
    mjesec = sadasnji_trenutak.month
    godina = sadasnji_trenutak.year

    sat  =sadasnji_trenutak.hour
    minuta = sadasnji_trenutak.minute
    sekunda = sadasnji_trenutak.second

    broj_R = f'{dan}.{mjesec}.{godina}.  {sat}:{minuta}:{sekunda}\nBroj računa: {broj_racuna}\n'
    return broj_R

for i in range(5):
    broj_rac = i+1
    sleep(1.5)
    print(generiraj_račun(broj_rac))
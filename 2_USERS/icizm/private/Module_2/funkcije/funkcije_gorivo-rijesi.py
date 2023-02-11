''' aplikacija za preračunavanje potrošnje goriva automobila u kune uz mogućnost izbora izračuna koliko maksimalno auto smije trošiti na 100km, ako je ciljana mjesečna potrošnja X kuna'''
import datetime as dt

def fuel_consumption(km):
    sadasnji_trenutak = dt. datetime.now()

    day = sadasnji_trenutak.day
    month = sadasnji_trenutak.month
    year = sadasnji_trenutak.year
    


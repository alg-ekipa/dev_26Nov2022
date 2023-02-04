# funkcija koja vraća vrijednost (znakovni niz) i ima ulazni argument


def dohvati_pozdrav(ime):
    return f' Dobar dan, {ime}'

poruka = dohvati_pozdrav ('Igor')
print (poruka)
poruka_marko = dohvati_pozdrav ('Marko')

print (poruka_marko)

#import math as m
from math import pi, pow

# korištenje i funkcije power iz math
def racunaj_povrsinu_kruga(r):
    #return m.pow(r,2)*m.pi
    return pow(r,2)*pi

P= racunaj_povrsinu_kruga(4)

print(P)
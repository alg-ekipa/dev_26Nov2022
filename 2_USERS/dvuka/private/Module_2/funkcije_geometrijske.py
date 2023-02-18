#import math as m
from math import pi, pow, sqrt

# korištenje i funkcije power iz math
def racunaj_povrsinu_trokuta(a):
    #return m.pow(r,2)*m.pi
    return pow(a,2)*sqrt(3)/4

def racunaj_visinu_trokuta(a):
    #return m.pow(r,2)*m.pi
    return a*sqrt(3)/2








a=input('upisi duljinu stranice jednakostranicnog trokuta: ')

a=int(a)


P= racunaj_povrsinu_trokuta(a)
V= racunaj_visinu_trokuta(a)

print (f'Povrsina jednakostranicnog trokuta duljine stranice {a} je {P}, a visina na stranicu {a} je {V}')
print()
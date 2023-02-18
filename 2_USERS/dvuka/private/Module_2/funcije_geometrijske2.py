import math                 #import math as m će skratitit pisanje na m.e,  m.pi,....

print(math.e)
print(math.pi)

# koristenje konstante pi

def racunaj_povrsinu_kruga(r):
    P=r**2*math.pi
    return P

povrsina_kruga=racunaj_povrsinu_kruga(4)

print(f'Povrsina kruga iznosi {povrsina_kruga}).')
print()

#korištenje i funkcije power iz math

def racunaj_povrsinu_kruga(r):
    return math.pow(r,2)*math.pi

P= racunaj_povrsinu_kruga   #ili P=racunaj_povrsinu_kruga(4)   print(P)
print(P(4))
print()

# ako dodamo naredbu 'from math import e, pi, pow' ne trebamo više pisati math.pi nego samo pi..

#izraditi funkcije za izračun površine i visine jednakostraničnog trokuta, kasnije u glavnom programu ih ispišite

import math
from math import sqrt, pow 

def povrsina_jednakostranicnog_trokuta(a):
    P=round(pow(a,2)*sqrt(3)/4,2)
    return P
def visina_jednakostraničnog_trokuta(a):
    v=round(a*sqrt(3)/2,2)
    return v

a=float(input('Unesi stranicu a: '))
print(f'Površina jednakostraničnog trokuta iznosi {povrsina_jednakostranicnog_trokuta(a)}, a visina {visina_jednakostraničnog_trokuta(a)}')
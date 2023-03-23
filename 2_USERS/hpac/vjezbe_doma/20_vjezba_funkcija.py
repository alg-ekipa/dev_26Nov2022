import math

def pov_kruga(r):
    P = r**2*math.pi
    return P

p = pov_kruga(5)
print(round(p,2))

def povrsina (r):
    return math.pow(r,2)*math.pi

p = povrsina

print(p(5))

from math import pi, pow    # na ovaj način pozivamo samo te funkcije, troši puno manje resursa, nego li kada idemo IMPORT MATH

def povrsina_kruga(r):
    P = r**2*pi
    return P

povrsina_kr = povrsina_kruga(4)
print(povrsina_kr)

def povrsina_kruga(r):
    return pow(r,2)*pi

pov = povrsina_kruga
print(round(pov(3),2))
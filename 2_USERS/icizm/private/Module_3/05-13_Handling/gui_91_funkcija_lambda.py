# 'Obična' funkcija

def povecaj_za_10(a):
    a+=10
    return a

print(povecaj_za_10(18))

# Lambda funkcija - spoj varijable i funkcije
# 'anonimna' funkcija - nema imena, nema return, ono što vraća ide u varijablu 

x = lambda a: a + 10 
print(x(18))

y = lambda a, b: a*b
print(y(5,7))
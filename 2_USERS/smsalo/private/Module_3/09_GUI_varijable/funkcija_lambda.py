#obična funkcija

def povecaj_za_10(a):
    a+=10
    return a

print(povecaj_za_10(18))

#lambda funkcija - spoj varijable i funkcije
#zove se i anonimna funkcija jer nema imena, return, samo joj treba varijabla

x=lambda a: a+10
print(x(18))            #dodajemo argument

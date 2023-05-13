def povecaj_za_10(a):
    a+=10
    return a


print(povecaj_za_10(18))


# Lambda funkcija  - spoj varijable i funkcije


x = lambda a: a+10

# Lambda funkcija se zove još i anonimna funkcija jer nema imena i nema return
# ono što vraća odmah ide u varijablu

print (x(18))


y= lambda a, b : a*b 
print (y(5,7))
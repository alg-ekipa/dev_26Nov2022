# Bez rekurzije, for petlja
'''def  faktorijeli(n):
    rez = 1
    for i in range(n):
        rez = rez * (i+1)

    return rez

print(faktorijeli(10))
'''

def faktorijeli(n):
    if n < 2:
        rez = 1
    else:
        rez = n*faktorijeli(n-1)
        print(rez)
    return(rez)

print(faktorijeli(10))
def faktorijeli(n):
    if n < 2: 
        rez = 1
    else: 
        rez = n*faktorijeli(n-1)
        print(rez)
    return(rez)

print(faktorijeli(10))
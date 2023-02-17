'''
napisati program koji od korisnika ocekuje upis 2 broja (jedan po jedan broj)
brojeve pokusajte zbrojiti i ispisite rezultat



a = input("Upiši a:")   
b = input("Upiši b:")   
c = a + b               # ne zbraja dobro jer imput je automatski STR
print(f"rezultat je {c}")

'''

a = int(input("Upiši a:") )   #definirali smo unos koa int - Casting se zove proces
b = int(input("Upiši b:") )
c = a + b               
print(f"rezultat je {c}")
'''
Napisati program koji od korisnika ocekuje:
-upis dužina stranica pravokutnika
-izračunati i ispisati opseg i površinu pravokutnika
'''


a = int(input("Unesi duljinu stranice a:") )   
b = int(input("Unesi duljinu stranice b:") )
o = 2*(a + b) 
p = a*b             
print(f"Opseg pravokutnika je {o}, a površina je {p}")
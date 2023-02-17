'''
Napisati program u koji korisnik unosi cijeli broj.
Provjeriti i ispisati jeli uneseni broj paran.
'''

a=int(input("Unesi broj:"))

if a%2 == 0:
    print(f"broj {a} je paran")
else:
    print(f"broj {a} nije paran")
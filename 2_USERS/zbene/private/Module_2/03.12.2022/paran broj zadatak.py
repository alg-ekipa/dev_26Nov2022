#Napisati program u koji korisnik unosi cijeli broj. Provjeriti i ispisati je li uneseni broj paran?
broj = int(input("Upišite cijeli broj: "))
if broj %2 == 0:
    print("Broj je paran")
else:
    print("Broj nije paran")
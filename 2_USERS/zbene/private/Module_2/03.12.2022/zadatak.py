#Napisati program koji od korisnika očekuje upis 2 broja (prvo prvog broja pa onda drugog, jedan po jedan). Brojeve pokušajte zbrojiti i ispišite rezultat

a = int(input("Upiši prvi od dva broja:"))
b = int(input("Upiši drugi od dva broja:"))

#Po default-u ono što dobivamo naredbom "input()" je TEKST (string)!!

print("Rezultat je:",a+b)
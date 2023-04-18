#Napisati python program koji od korisnika očekuje upis troznamenkastog broja. Program treba provjeriti je li barem jedna od tih znamenki parna.

broj = int(input("Upiši troznamenkasti broj: "))

if broj>=100 and broj<=999 and (broj//100)%2==0 or (broj%100)//10%2==0 or (broj%10)%2==0:
    print(f"Barem jedna od znamenki broja {broj} je parna.")
elif broj<100 or broj>999:
    print(f"Uneseni broj {broj} nije troznamenkast.")
else:
    print(f"Nijedna znamenke broja {broj} nije parna.")
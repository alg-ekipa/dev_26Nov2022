#Napisati python program koji od korisnika očekuje upis troznamenkastog broja. Program treba provjeriti i ispisati jesu li sve znamenke broja parne.

broj = int(input("Upiši troznamenkasti broj: "))

if broj>=100 and broj<=999 and (broj//100)%2==0 and (broj%100)//10%2==0 and (broj%10)%2==0:
    print(f"Sve znamenke broja {broj} su parne.")
elif broj<100 or broj>999:
    print(f"Uneseni broj {broj} nije troznamenkast.")
else:
    print(f"Neke znamenke broja {broj} nisu parne.")
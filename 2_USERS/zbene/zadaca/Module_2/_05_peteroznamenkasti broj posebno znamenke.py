#Napisati python program koji od korisnika očekuje upis peteroznamenkastog broja. Program treba provjeriti i ispisati peteroznamenkasti broj i svaku znamenku zasebno.

broj = int(input("Upiši peteroznamenkasti broj: "))

peteroznamenkasta = broj//10000
četveroznamenkasta = (broj%10000)//1000
troznamenkasta = (broj%1000)//100
dvoznamenkasta = (broj%100)//10
jednoznamenkasta = broj%10

if broj>=10000 and broj<=99999:
    print(f"Znamenke broja {broj} su: {peteroznamenkasta}, {četveroznamenkasta}, {troznamenkasta}, {dvoznamenkasta} i {jednoznamenkasta}.")
else:
    print(f"Uneseni broj {broj} nije peteroznamenkast.")
'''

5eroznamenkasti i ispisati svaku znamenku posebno

'''

duzina_broja=0

while duzina_broja != 5:
    peteroznamenkasti_broj=int(input("Upiši peteroznamenkasti cijeli broj: "))
    duzina_broja=len(str(peteroznamenkasti_broj))
    if duzina_broja != 5:
        print("Broj koji ste unijeli nije peteroznamenkasti!")
else:

    znamenka_1=peteroznamenkasti_broj//10000
    znamenka_2=(peteroznamenkasti_broj//1000)%10
    znamenka_3=(peteroznamenkasti_broj//100)%10
    znamenka_4=(peteroznamenkasti_broj//10)%10
    znamenka_5=peteroznamenkasti_broj%10

print(f"Prva znamenka je {znamenka_1}")
print(f"Prva znamenka je {znamenka_2}")
print(f"Prva znamenka je {znamenka_3}")
print(f"Prva znamenka je {znamenka_4}")
print(f"Prva znamenka je {znamenka_5}")
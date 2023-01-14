'''
3 znamenkastog broja
- provjeriti jesu li sve znamenke broja parne
- je li barem jedna parna

'''

duzina_broja=0
broj_parnih_znamenki=0

while duzina_broja != 3:
    troznamenkasti_broj=int(input("Unesi troznamenkasti broj: "))
    duzina_broja=len((str(troznamenkasti_broj)))
    if duzina_broja != 3:
        print("Niste unije broj sa 3 znamenke!")

    else:
        if (troznamenkasti_broj//100)%2==0:
            broj_parnih_znamenki +=1
        if ((troznamenkasti_broj%100)//10)%2==0 :
            broj_parnih_znamenki +=1
        if (troznamenkasti_broj%10)%2==0:
            broj_parnih_znamenki +=1

print(f"{broj_parnih_znamenki} znamenka/e su parne.")
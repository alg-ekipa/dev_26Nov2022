a=int(input("Unesite 3-znamenkasti broj"))
if (a//100)%2==0 or (a%100//10)%2==0 or (a//10)%2==0:
    print ("Barem jedna znamenka je parna")
a=int(input("Unesite 3-znamenkasti broj"))
if (a//100)%2==0 and (a%100//10)%2==0 and (a//10)%2==0:
    print ("Sve znamenke su parne")
else:
    print ("Sve znamenke nisu parne")
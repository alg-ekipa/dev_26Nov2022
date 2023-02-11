#Kalkulator
izbor = 0
while 1:
    print ("Dobrodosli u kalkulator.py!")
    print ("Izaberi racunsku operaciju:")
    print (" ")
    print ("1) Zbrajanje")
    print ("2) Oduzimanje")
    print ("3) Mnozenje")
    print ("4) Dijeljenje")
    print ("5) Izlaz iz kalkulatora")
    print (" ")
    izbor = int(input("Unesi broj ispred zeljene operacije:") )   

    if izbor == 1:     
        prib1 = int(input("Zbroji ovaj broj: "))
        prib2 = int(input("s ovim brojem: "))
        print (prib1, "+", prib2, "=", prib1 + prib2 )   

    elif izbor == 2:     
        oduz1 = int(input("Oduzmi od ovog broja: "))
        oduz2 = int(input("ovaj broj: "))
        print (oduz1, "-", oduz2, "=", oduz1 - oduz2)

    elif izbor == 3:    
        mnoz1 = int(input("Pomnozi ovaj broj: ") )  
        mnoz2 = int(input("sa ovim brojem: "))
        print (mnoz1, "*", mnoz2, "=", mnoz1 * mnoz2)

    elif izbor == 4:    
        dij1 = int(input("Podijeli ovaj broj: "))
        dij2 = int(input("sa ovim brojem: "))
        print (dij1, "/", dij2, "=", dij1 / dij2)

    elif izbor == 5:    
        break

print ("Hvala sto ste koristili kalkulator.py!")
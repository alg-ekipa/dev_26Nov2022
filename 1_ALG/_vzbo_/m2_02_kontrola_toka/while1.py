# Password

password = ""
while password != "tajno":
    password = input("Unesite lozinku: ")
    if password == "tajno":
        print("Upisali ste  tocnu lozinku")
    else:
        print("upisali ste pogresnu lozinku-pokusajte ponovno")
        print ("Igra pogadjanja brojeva")
print ("Za prekid igre unesite 0")
 
# Pogodi broj (zadan je)

pogodi=17
 
while 1:
    broj=int(input("Unesite broj: "))
    if broj==pogodi:
        print ("Pogodili ste zadani broj cestitamo!")
        #break
        broj=0
    elif broj==0:
        break
    elif broj > pogodi:
        print ("Broj je veci od zadanog, pokusajte ponovo")
    elif broj < pogodi:
        print ("Broj je manji od zadanog, pokusajte ponovo")


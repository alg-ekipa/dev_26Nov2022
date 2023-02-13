'''
print("1: DULJINA km --> milje")
print("2: TEMPERATURA C --> F")

conversion = int(input("Odaberite konverziju: "))

if conversion == 1:
    km = float(input("unesite duljinu u km: "))
    milje = km *0.6214
    print (f"Duljina od {km} km iznosi {milje} milja")
    

if conversion == 2:
    c = float(input("unesite temperaturu u stupnjevima C: "))
    f = c*(9/5) +32
    print (f"Temperatura od {c} C iznosi {f} F")


 #Zadatak za konverziju iz kilometre u milje 
milja = 0.6214
km_milja = int(input("Unesite broj: "))
print(km_milja * milja)

#Zadatak kilograme u funte 
funte = 2.2046
kg_pounds = int(input("Unesite broj: "))
print(kg_pounds * funte)


print('1 km -> milje\n2 C -> F\n3 kg -> pound\n4 L -> US Galon\n5 kW -> KS')
pretvorba = int(input('Unesite željenu konverziju: '))
print(pretvorba)
if pretvorba == 1:
    unos_km = float(input('Unesi km: '))
    milje = unos_km / 0.6214
    print(f'{unos_km}km je {milje} milja.')
elif pretvorba == 2:
    unos_celz = float(input('Unesi stupnjeve u Celsiusu: '))
    farenh = unos_celz * (9/5) + 32
    print(f'{unos_celz} C je {farenh} F.')

'''
while True:
    tip = int(input("Odaberite koji tip konverzije želite?\n 1. km u milje \n 2. °C u °F \n 3. kg u funtu \n 4. Litra u US galon \n 5. kW u KS\n"))
    if tip == 1:
        while True:
            smjer = int(input("Koji smjer konverzije želite? \n 1. km u milje \n 2. milje u km \n"))
            if smjer == 1:
                unos = float(input("Unesite udaljenost u km \n"))
                print(f"Udaljenost od {unos} km  je {unos * 0.6214} milja")
                break
            elif smjer == 2:
                unos = float(input("Unesite udaljenost u miljama \n"))
                print(f"Udaljenost od {unos} milja  je {unos / 0.6214} km")
                break
            else:
                continue
    elif tip == 2:
        while True:
            smjer = int(input("Koji smjer konverzije želite? \n 1. °C u °F \n 2. °F u °C \n"))
            if smjer == 1:
                unos = float(input("Unesite temperaturu u °C \n"))
                print(f"Temperatura od {unos}")
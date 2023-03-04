def kreiraj_racun(brojac_racuna, datum, pdv):
    
    stavke = {}

    while True:
        proizvod = input("Unesi prooizvod: ")
        cijena = float(input("Unesi cijenu: "))
        stavke[proizvod] = cijena #ovako punimo rijecnik
        if not input("Unos nove stavke? Za NE pritisnite Enter"):   #tako izlazi iz petlje
            break
    
    return stavke


brojac_r = 1
PDV = 0.25
datum = "4.03.2023."

racuni = {}

while True:
    kreirani_racun = kreiraj_racun(brojac_r, datum, PDV)
    racun_broj = f"R-{brojac_r}-2023"
    brojac_r +=1
    racuni[racun_broj] = kreirani_racun

    if not input("želite li novi racun? (Enter ako ne.)"):
        break

for rbr, racun in racuni.items():
    print(rbr, racun)






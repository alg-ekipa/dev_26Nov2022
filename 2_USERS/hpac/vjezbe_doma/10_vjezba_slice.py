brojevi = []

for i in range(101):
    brojevi.append(i)

#print(brojevi)

# SLICE-anje liste: "izrezuje" dijelo liste [START : STOP : KORAK] - s kojim zapošinje, završava (ali nije uključen) i koliki mu je "korak"

izdvojeni_brojevi = brojevi[10:30]
print(izdvojeni_brojevi)

izdvojeni_brojevi2 = brojevi[20:]    
print(izdvojeni_brojevi2)

izdvojeni_brojevi3 = brojevi[:25:2]
print(izdvojeni_brojevi3)

izdvojeni_brojevi4 = brojevi[::-1]
print(izdvojeni_brojevi4)

izdvojeni_brojevi5 = brojevi[-2::]
print(izdvojeni_brojevi5)

izdvojeni_brojevi6 = brojevi[-35::1]
print(izdvojeni_brojevi6)

izdvojeni_brojevi7 = brojevi[:-3:1]
print(izdvojeni_brojevi7)
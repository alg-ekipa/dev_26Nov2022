brojevi = []

for i in range(101):
    brojevi.append(i)

print(brojevi)
print()

# sintaksa SLICE-anje liste:   brojevi[START : STOP : STEP]

#print(brojevi[20 : 51 : 5])
#print()

#print(brojevi[20 : 51 : 1])
#print()

izdvojeni_brojevi = brojevi[20 : 51 : 5]
#print(izdvojeni_brojevi)

podlista1 = brojevi[20 : ]
print(podlista1)
print()

podlista2 = brojevi[ : 41]
print(podlista2)
print()

brojevi_obrnuto = brojevi[51 : 20 : -1]
print(brojevi_obrnuto)
print()

brojevi_obrnuto = brojevi[::-1]
print(brojevi_obrnuto)
print()

podlista3 = brojevi[-2 :]  # od 99 do 100
print(podlista3)
print()

podlista4 = brojevi[: -2]  # od početka do 98
print(podlista4)
print()

podlista5 = brojevi[: -3 : -1]  # kreće od kraja sve dok ne dođe do trećeg elemnta od ktraja (98) ali on NIJE uključen 
print(podlista5)
print()

podlista6 = brojevi[-3 : : -1]  # kreće od  -3, odnosno trećeg elementa od kraja
print(podlista6)
print()
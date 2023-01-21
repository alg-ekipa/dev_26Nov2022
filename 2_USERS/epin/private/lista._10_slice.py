brojevi = []

for i in range(1, 101):
    brojevi.append(i)

#print(brojevi)

#sintaksa Slice-anja liste brojevi; brojevi[START : STOP : STEP]

izdvojeni_brojevi = brojevi[20 : 51 : 1]
#print(izdvojeni_brojevi)

podlista1 = brojevi[20 : ]
#print(podlista1)

podlista2 = brojevi[ : 41]
#print(podlista2)

brojevi_obrnuto = brojevi[::-1]
#print(brojevi_obrnuto)


podlista3 = brojevi[-2 :]
#print(podlista3)

podlista4 = brojevi[ :-2]
#print(podlista4)

podlista5 = brojevi[: -3 : -1]
#print(podlista5)

podlista6 = brojevi[-3 : : -1]
print(podlista6)
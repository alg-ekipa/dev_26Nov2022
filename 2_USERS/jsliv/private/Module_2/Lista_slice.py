brojevi = []

for i in range(101):
    brojevi.append(i)

print(brojevi)

#sintaksa slice: brojevi[start : stop : step]

print(brojevi[20 : 51 : 5])

izdvojeni_brojevi = brojevi[20 : 51 : 1]
print(izdvojeni_brojevi)

podlista1 = brojevi[20:]

print(podlista1)

podlista2 = brojevi[ : 41]
print(podlista2)

brojevi_obrnuto = brojevi[51 : 19 : -1]
print(brojevi_obrnuto)

brojevi_obrnuto = brojevi[:: -1]
print(brojevi_obrnuto)

podlista3 = brojevi[-2 :]
print(podlista3)

podlista4 = brojevi[:-2]
print(podlista4)

podlista5 = brojevi[: -3 : 2]
print(podlista5)



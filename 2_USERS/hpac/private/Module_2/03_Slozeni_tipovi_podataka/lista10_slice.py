brojevi = []
for i in range(101):
    brojevi.append(i)

#print(brojevi)

# sintaksa SLICE-anja liste: brojevi[START : STOP : STEP]

izdvojeni_brojevi = brojevi[20 : 51 : 5]
print(izdvojeni_brojevi)

podlista1 = brojevi[20 : ]
print(podlista1)

podlista1 = brojevi[ : 41]
print(podlista1)

brojevi_obrnuto = brojevi[::-1]
print(brojevi_obrnuto)

#u ovim varijantama gleda indeks člana od nazad
podlista3 = brojevi[-2:] #od 99 do 100
print(podlista3)

podlista4 = brojevi[:-2] #od početka do 98
print(podlista4)

podlista5 = brojevi[:-3:-1] #kreće od kraja sve dok ne dođe do trećeg elementa od kraja (98), ali on NIJE uključen (STOP nije uključen)
print(podlista5)

podlista6 = brojevi[-3 : : -1] #kreće od -3, tj trećeg elementa od kraja
print(podlista6)

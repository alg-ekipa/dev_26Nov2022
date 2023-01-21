brojevi=[]
for i in range (101):
    brojevi.append(i)

print(brojevi)

# sintaksa SLICE-anja liste: brojevi [start:sop:step]

izdvojeni_brojevi=brojevi[20:51:5]
print(izdvojeni_brojevi)
print()

podlista_1=brojevi[20: ] #ide do kraja liste
print(podlista_1)
print()

podlista_2=brojevi[ :41] # od početka do 40
print(podlista_2)
print()

brojevi_obrnuto=brojevi[50:19:-1]
print(brojevi_obrnuto)
print()

brojevi_obrnuto_lista=brojevi[::-1]
print(brojevi_obrnuto_lista)
print()

podlista_3=brojevi[-2:] #print zadnja 2 u listi
print(podlista_3)
print()

podlista_4=brojevi[:-2] #print od početka do zadnja 2 u listi
print(podlista_4)
print()

podlista_5=brojevi[:-3:-1] #kreće od kraja sve dok ne dođe do trećeg elemeta od kraja (98), ali on nije uključen
print(podlista_5)

podlista_6=brojevi[-3::-1] #kreće od -3 odnosno trećeg elementa od kraja 
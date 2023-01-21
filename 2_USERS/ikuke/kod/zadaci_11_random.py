import random

broj = random.randint(0,10)


# kreiramo listu od 20 članova koje nasumično bira u rasponu od 0 do 30

lista=[]
for i in range(20):
    broj = random.randint(0,30)
    print (broj)
    lista.append(broj)

print(lista)




#nasumično izabiranje indeksa člana i ispis člana koji je pod tim indeksom

broj = random.randint(0,20)
clan=lista[broj]

print('nasumično izabrani član liste je:', clan)
print('indeks odabranog člana liste je', broj)



#nasumično izabiranje jednog člana liste i ispis člana koji je pod tim indeksom

broj = random.randint(0,20)
clan=lista[broj]

print('nasumično izabrani član liste je:', clan)
print('indeks odabranog člana liste je', broj)
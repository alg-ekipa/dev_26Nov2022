import random

# kreiramo listu od 20 članova koje nasumično bira u rasponu od 0 do 30

lista_random=[]

for i in range(20):
    broj = random.randint(0,30)
    #print(broj)
    lista_random.append(broj)
print(lista_random)



# nasumično izabiranje jednog člana liste
print()

random_clan=random.choice(lista_random)
print(f"Nasumično izabran član liste je {random_clan}.")
print(f"Index tog člana je {lista_random.index(random_clan)}.")


# nasumično izabiranje indexa i ispis člana koji je pod tim indexom
print()

random_index=random.randint(0,19)
print(f"Nasumično izabran index je {random_index}.")
print(f"Član s tim indexom je {lista_random[random_index]}.")

slovo=input("Unesi slovo ")
print(slovo.upper())

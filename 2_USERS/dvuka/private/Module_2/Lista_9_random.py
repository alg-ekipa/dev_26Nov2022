import random

#Kreiramo listu od 20 članova koje nasumično bira u rasponu od 0 do 30

lista_random=[]

for i in range(20):
    broj=random.randint(0,30)
    print(broj, end=' ')
    lista_random.append(broj)

    print(lista_random)

    #Nasumično izabiranje jednog člana liste i ispis njegovog indeksa

    random_clan=random.choice(lista_random)
    print(f'Nasumično izabran član liste: {random_clan}')
    print(f'Indeks tog člana je {lista_random.index(random_clan)}')

    #Nasumično izabiranje indeksa i ispis člana koji je pod tim indeksom

    random_index=random.randint(0,19)
    print(f'Nasumično izabran član liste: {random_index}')
    print(f'Član s tim indeksom je {lista_random[random_index]}')

slovo=input('Unesi slovo')
print(slovo.upper())

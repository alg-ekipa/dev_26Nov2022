import random 
'''
broj = random.randint(0, 10) #ako želimo bilo što uzeti iz random modula pišemo random. RANDINT - random integer
print(broj)
'''
#idemo listu napuniti sa rendom brojevima
#^ ovo izvrtimo onoliko puta koliko nam lista ima članova
#Kreirajmo listu od 20 članova koje nasumično biva u rasponu od 0 do 30 


lista_random = []

for i in range(20):
        broj = random.randint(0, 30)
        #print(broj, end = ' ')
        lista_random.append(broj)
print(lista_random) #svaki put kad se provrti program on odabere nove random brojeve

#Nasumično izabiranje jednog člana liste i ispis njegovog indeksa

random_clan = random.choice(lista_random)

print(f'Nasumično izabran član liste: {random_clan}')
print(f'Indeks tog člana je {lista_random.index(random_clan)}')

#Napisati koji je indeks nasumično odabranog člana i zatim nasumično izaberemo idex i odaberemo koji je to član

random_indeks = random.randint(0, 19)
print(f'Nasumično izabran indeks liste: {random_indeks}')
print(f'Član s tim indeksom je {lista_random[random_indeks]}')


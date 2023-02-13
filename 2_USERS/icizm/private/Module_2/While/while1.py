#while petlja ima uvijet i nakon provjere se vraća na početak

brojevi = []
for i in range(1, 21): #inicijaliziramo početak i kraj
    brojevi.append(i)

for broj in brojevi:
    print(broj, end=' ')
#print(brojevi)
i = 0  #početni uvijet je postavljen izvan
while i < len(brojevi):  #možemo postaviti granicu ali moramo biti oprezni
    print(brojevi[i]) 
    i += 1
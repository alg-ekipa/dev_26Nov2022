import math     # ako stavimo math as m, onda umjesto funkcije MATh pišemo M


# Uvoz konstante PI iz MATH
def racunaj_povrsinu_kruga(r):
    P = r**2*math.pi
    return P

povrsina_kruga = racunaj_povrsinu_kruga(4)

print(f'Povrsina kruga iznosi {round(povrsina_kruga,2)} cm2')

# korištenje i funkcije power i math
def racunaj_povrsinu_kruga(r):
    return math.pow(r,2)*math.pi

P = racunaj_povrsinu_kruga

print(P(4))  #na ovaj način argument je tu definiran a ne kod definiranje varijable 'P', kao primjer iznad
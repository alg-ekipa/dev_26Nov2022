#import math as m # - svugdje umjesto math. pišemo m. 
from math import pi, pow  #ne trebamo ispred pi i pow pisati math., tj. m.

# korištenje konstante pi iz math 

def racunaj_povrsinu_kruga(r):
    P = r**2*pi   #P se nalazi unutar funkcije i ne može se isprinati
    return P

povrsina_kruga  = racunaj_povrsinu_kruga(4)

print(f'Povrsina kruga iznosi {round(povrsina_kruga,2)}cm2')
print()

# korištenje i funkcije power iz math

def racunaj_povrsinu_kruga(r):
     return pow(r, 2) * pi

P = racunaj_povrsinu_kruga(4)

print(P)
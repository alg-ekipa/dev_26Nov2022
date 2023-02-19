tekst ='''
Lorem ipsum dolor sit amet, consectetur adipiscing elit.  
Vivamus cursus nulla arcu, sollicitudin aliquet dui tempus non.  
Mauris vitae porttitor erat. Morbi vitae diam et urna volutpat hendrerit.  
Donec aliquam velit a venenatis bibendum.  
Nullam orci erat, bibendum in aliquam eget, finibus eu massa.  
Duis tincidunt turpis eget elementum dapibus.  
Fusce congue ac elit gravida faucibus. Pellentesque bibendum suscipit ullamcorper.  
Nulla non nibh elementum, aliquet dui ac, pharetra eros.  
Quisque vel mollis orci.  
Nunc porttitor, risus eu sagittis mollis, lorem mauris varius leo,  
faucibus semper dui dui vel est.  
Donec rutrum velit vitae ex congue, vitae rhoncus nunc dictum.  
Suspendisse imperdiet consequat pellentesque.  
Curabitur condimentum eget enim at auctor.  
In hac habitasse platea dictumst. Fusce semper id augue non sodales.  
Cras non dui quam. Mauris porttitor mauris sit amet ligula vestibulum  
sodales egestas vitae ligula. Nam eleifend sed turpis accumsan laoreet.  
Aliquam vel venenatis nulla, et tristique nunc.  
Mauris rhoncus tortor interdum nulla sollicitudin convallis.  
Fusce euismod dui non metus finibus, et vehicula risus egestas.  
In non fermentum lorem. Proin et magna tellus.  
Nullam rhoncus luctus lorem, vel rutrum turpis sollicitudin vel.  
Cras sit amet sapien vel orci pretium finibus consectetur eu enim.  
Cras eget hendrerit sem. Sed ullamcorper sagittis malesuada.  
Aenean auctor turpis quis mi egestas malesuada.  
Praesent ac tortor vel odio lacinia tempus 
'''
#koliko puta se ponavlja neka riječ. Trebamo napraviti najprije listu riječi, riješiti problem velikih i malih slova, 

'''testni_string ='Jedan dva TRI'
testni_string = testni_string.lower()
razdvojeni = testni_string.split(' ')
print(razdvojeni)'''

tekst1 = tekst.lower()
lista_rijeci = tekst1.split(' ')

for rijec in lista_rijeci:
    if '.' in rijec:
        lista_rijeci[lista_rijeci.index(rijec)] = rijec.replace('.','') #pronađi indeks te riječi i u njemu zamijeni traženu stvar
    elif ',' in rijec:
        lista_rijeci[lista_rijeci.index(rijec)] = rijec.replace(',','')
    elif '\n' in rijec:
        lista_rijeci[lista_rijeci.index(rijec)] = rijec.replace('\n','')

unesi_rijec = input('Koliko puta se ponavlja ova riječ: ')
brojac = 0

for rijec in lista_rijeci: 
    if rijec == unesi_rijec:
        brojac += 1

print(f'Riječ {unesi_rijec} u "Lore ipsum" tekstu ponavlja se {brojac}')
   
#print(lista_rijeci)

'''testni = '\nrijec druga treca.'
testni = testni.split(' ')
print(testni[0].replace('\n',''))
print(testni[2].replace('.',''))'''

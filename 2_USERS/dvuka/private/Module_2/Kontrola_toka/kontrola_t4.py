tekst='''

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
#print(tekst)

testni='jedan Dva TRI'
testni=testni.lower()
print(testni)
razdvojeni=testni.split(' ')
print(razdvojeni)

tekst1=tekst.lower()
lista_rijeci=tekst1.split(' ')
print(lista_rijeci)

'''
testni='\nrijec druga treca.'
testni=testni.split(' ')
print(testni[0].replace('\n', ''))
print(testni[2].replace('.', ''))
'''

for rijec in lista_rijeci:
    if'.' in rijec:
        lista_rijeci[lista_rijeci.index(rijec)]=rijec.replace('.','')
    elif',' in rijec:
        lista_rijeci[lista_rijeci.index(rijec)]=rijec.replace(',','')
    elif'\n' in rijec:
        lista_rijeci[lista_rijeci.index(rijec)]=rijec.replace('\n','')

print(lista_rijeci)
'''
a = input("Unesi rijec: ")

broj = lista_rijeci.count(a)

if a in tekst:
    print(f"Rijec {a} se nalazi u tekstu {broj} puta")
else:
    print("nema rijeci")
'''

trazena_rijec=input('Unesi trazenu rijec: ')
brojac =0

for rijec in lista_rijeci:
    if rijec==trazena_rijec:
        brojac+=1
print(f'Rijec {trazena_rijec} pojavljuje se u tekstu {brojac}puta.')




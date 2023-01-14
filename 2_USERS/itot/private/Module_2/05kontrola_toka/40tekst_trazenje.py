tekst = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit.

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

Praesent ac tortor vel odio lacinia tempus'''

testni = 'jedan dva tri'
razdvojeni = testni.split(' ') # split kod razmaka 
print (razdvojeni)
print(tekst)

'''
testni2 ='\nrijec druga treca.'
testni2 = testni2.split(' ')
print(testni2[0].replace('\n',''))
print(testni2[2].replace('.',''))'''


tekst1 = tekst.lower()
lista_rijeci = tekst1.split(' ')

for rijec in lista_rijeci:
    if '.' in rijec:
        lista_rijeci[lista_rijeci.index(rijec)] = rijec.replace('.','')
    elif ',' in rijec:
        lista_rijeci[lista_rijeci.index(rijec)] = rijec.replace(',','')
    elif '\n' in rijec:
        lista_rijeci[lista_rijeci.index(rijec)] = rijec.replace('\n','')
    elif '\n\n' in rijec:
        lista_rijeci[lista_rijeci.index(rijec)] = rijec.replace('\n\n','')

print(lista_rijeci)        

''' ovo mi ne radi, doma isprobati'''

#a verzija sa brojacem
a=0
for rijec in lista_rijeci:
    if rijec == 'lorem':
        a += 1
print(f'rijec lorem se u tekstu pojavljuje {a} puta')

# b verzija sa count
testna_rijec = input('unesi trazenu rijec: ')
broj_rijeci = lista_rijeci.count(testna_rijec)
print(f'rijec {testna_rijec} se u tekstu pojavljuje {broj_rijeci} puta')
tekst = '''
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
Praesent ac tortor vel odio lacinia tempus '''

#print(tekst)

testni = 'jedna dva TRI'
testni = testni.lower()
print(testni)
razdvojeni = testni.split(' ')
print(razdvojeni)
print()



tekst = tekst.lower()
razdvojeni_tekst = tekst.split(' ')
print(razdvojeni_tekst)

'''
testni1 = '\nrijec druga treca.'
testni1 = testni1.split(' ')
print(testni1[0].replace('\n',''))
print(testni1[2].replace('.',''))
'''

for rijec in razdvojeni_tekst:
    if '.' in rijec:
        razdvojeni_tekst[razdvojeni_tekst.index(rijec)] = rijec.replace('.', '')
    elif ',' in rijec:
        razdvojeni_tekst[razdvojeni_tekst.index(rijec)] = rijec.replace(',', '')
    elif '\n' in rijec:
        razdvojeni_tekst[razdvojeni_tekst.index(rijec)] = rijec.replace('\n', '')
print(razdvojeni_tekst)


rijec1 = 'lorem'
rijec2 = 'leo'

if rijec1 in razdvojeni_tekst:
    broj_rijeci1 = razdvojeni_tekst.count(rijec1)
if rijec2 in razdvojeni_tekst:
    broj_rijeci2 = razdvojeni_tekst.count(rijec1)    
print(f'Rijec {rijec1} u tekstu se nalazi {broj_rijeci1}')
print(f'Rijec {rijec2} u tekstu se nalazi {broj_rijeci2}')

trazena_rijec = input ('Unesi trazenu rijec: ')
brojac = 0

for rijec3 in razdvojeni_tekst:
    if rijec3 == trazena_rijec:
        brojac += 1 

print(f'Rijec {trazena_rijec} u tekstu se nalazi {brojac}')
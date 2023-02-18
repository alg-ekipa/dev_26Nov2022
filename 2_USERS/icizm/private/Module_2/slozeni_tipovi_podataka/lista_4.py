#zbroj brojeva od 1 do 20

# i je pomoćna varijabla - ITERATOR
#ako u range piše samo 1 broj onda se podrazumjeva od 0 do tog broja = nema START
#ako nema STEP on je 1

zbroj = 0

for i in range(21):
    print(i, end = ' ')
    zbroj= zbroj + i
    print(zbroj)
print(f'Završni zbroj je {zbroj}') #samo ovaj print je dovoljan za rješenje zadatka
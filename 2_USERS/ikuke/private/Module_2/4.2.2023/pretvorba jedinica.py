
#funkcije

def funkcija1():
    print('unesi snagu u kW:', end= ' ')
    snaga=int(input())
    snagaKS=float(snaga*1.341)
    print(f'snaga {snaga }kW je {snagaKS} KS')
    

def funkcija2():
    print('unesi snagu u kW:', end= ' ')
    snaga=int(input())
    snagaKS=float(snaga/1.341)
    print(f'snaga {snaga} KS je {snagaKS} kW')
 


def funkcija3():
    print('unesi iznos u kn:', end= ' ')
    snaga=int(input())
    snagaKS=round(float(snaga/7.5345),2)
    print(f'iznos {snaga} kn je {snagaKS} EUR')
  


def funkcija4():
    print('unesi iznos u EUR:', end= ' ')
    snaga=int(input())
    snagaKS=round(float(snaga*7.5345),2)
    print(f'iznos {snaga} EUR je {snagaKS} kn')
    

print('odaberite koji tip konverzije želite?')
print('1 - kW u KS')
print('2 - KS u kW')
print('3 - kn u EUR')
print('4 - EUR u kn')
izbor=int(input())


if izbor == 1:
    funkcija1()


if izbor == 2:

     funkcija2()


if izbor == 3:
   
  funkcija3()


if izbor == 4:
  funkcija4()


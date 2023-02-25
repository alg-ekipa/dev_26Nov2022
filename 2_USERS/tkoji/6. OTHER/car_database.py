vozni_park = {
    1 : ['Kamion', 'Iveco', 'OS 001 ZZ', 2015, 45000.00],
    2 : ['Kamion', 'Iveco', 'OS 002 ZZ', 2015, 47000.00],
    3 : ['Tegljač', 'MAN', 'RI 001 ZZ', 2018, 78000.00],
    4 : ['Tegljač', 'MAN', 'RI 002 ZZ', 2020, 97000.00],
    5 : ['Kombi', 'Mercedes Benz', 'ST 001 ZZ', 2013, 12000.00],
    6 : ['Kombi', 'Volkswagen', 'ST 002 ZZ', 2021, 35000.00],
    7 : ['Dostavno vozilo', 'Volkswagen', 'ZG 001 ZZ', 2010, 9000.00],
    8 : ['Dostavno vozilo', 'Volkswagen', 'ZG 002 ZZ', 2010, 9300.00],
}

print(vozni_park[3][-2])

for v in vozni_park.values():
  print(v)
  
for k in vozni_park.keys():
  print(k)

for k,v in vozni_park.items():
  print(k,v)

print(vozni_park.items())

print('ID\tTip\tProizvodac\tRegistracija\tGodina\tCijena')
print("_"*100)

for k,v in vozni_park.items():
    print(f'{k}', end='\t')
    for element in v:
        print(f'{element}', end='\t\t')
    print()

#IP = 172.24.0.1
adresa = 172.24.0.1

prvi_oktet = bin(172).replace('0b','')
drugi_oktet = bin (24).replace('0b','')
treći_oktet = bin(0).replace('0b','')
četvrti_oktet = bin(1).replace('0b','')

print(prvi_oktet)
print(drugi_oktet)
print(treći_oktet)
print(četvrti_oktet)

print('IPv4 adresa ovog računala je:','adresa')
print ('Binarni zapis IPv4 adrese je: ')
print ('Oktalni zapis IPv4 adrese je: ')
print('JHeksadecimalni zapis IPv4 adrese je: ')
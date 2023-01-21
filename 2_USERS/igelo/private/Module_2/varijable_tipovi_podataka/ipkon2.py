
a = '172.27.240.1'
print('IP Adresa je:', a)

prvi_oktet = bin(172).replace('0b','')
drugi_oktet =bin(27).replace('0b','.')
treci_oktet =bin(240).replace('0b','.')
cetvrti_oktet = bin(1).replace('0b','.')
print('Binarni zapis IP Adrese je:', ' ', prvi_oktet, drugi_oktet, treci_oktet, cetvrti_oktet, sep='')


prvi_oktet = oct(172).replace('0o','')
drugi_oktet =oct(27).replace('0o','.')
treci_oktet =oct(240).replace('0o','.')
cetvrti_oktet = oct(1).replace('0o','.')
print('Hexadecimalni zapis IP Adrese je:',' ', prvi_oktet, drugi_oktet, treci_oktet, cetvrti_oktet, sep='')


prvi_oktet = hex(172).replace('0h','')
drugi_oktet =hex(27).replace('0h','.')
treci_oktet =hex(240).replace('0h','.')
cetvrti_oktet = hex(1).replace('0h','.')
print('Oktalni zapis IP Adrese je:',' ' , prvi_oktet, drugi_oktet, treci_oktet, cetvrti_oktet, sep='')



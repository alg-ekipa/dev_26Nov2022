import socket
hostname = socket.gethostname()
## getting the IP address using socket.gethostbyname() method
ip_address = socket.gethostbyname(hostname)

print(ip_address)
print()

ip_split = ip_address.split('.')
#print(ip_split)

bin_1 = bin(int(ip_split[0])).replace('0b','')
bin_2 = bin(int(ip_split[1])).replace('0b','')
bin_3 = bin(int(ip_split[2])).replace('0b','')
bin_4 = bin(int(ip_split[3])).replace('0b','')

print(f'IP adresa {ip_address} prikazana u binarnom kodu je {bin_1}.{bin_2}.{bin_3}.{bin_4}')
print()

hex_1 = hex(int(ip_split[0])).replace('0x','')
#print(hex_1)
hex_2 = hex(int(ip_split[1])).replace('0x','')
hex_3 = hex(int(ip_split[2])).replace('0x','')
hex_4 = hex(int(ip_split[3])).replace('0x','')

print(f'IP adresa {ip_address} prikazana u binarnom kodu je {hex_1}.{hex_2}.{hex_3}.{hex_4}')
print()

oct_1 = oct(int(ip_split[0])).replace('0o','')
#print(hex_1)
oct_2 = oct(int(ip_split[1])).replace('0o','')
oct_3 = oct(int(ip_split[2])).replace('0o','')
oct_4 = oct(int(ip_split[3])).replace('0o','')

print(f'IP adresa {ip_address} prikazana u binarnom kodu je {oct_1}.{oct_2}.{oct_3}.{oct_4}')
print()

''''
Provjerite svoju IP adresu i pretvorite ju u binarnu i hexidekadsku


'''

#uvoz IP adrese računala
import socket
hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)
print(f"Tvoja IP adresa je: {IPAddr}")

IPAddr_oktet = IPAddr.split(".")

prvi_oktet_bin =  bin(int(IPAddr_oktet[0])).replace('0b','')
drugi_oktet_bin =  bin(int(IPAddr_oktet[1])).replace('0b','')
treci_oktet_bin = bin(int(IPAddr_oktet[2])).replace('0b','')
cetvrti_oktekt_bin = bin(int(IPAddr_oktet[3])).replace('0b','')

print(f'IP adresa binarno: {prvi_oktet_bin}.{drugi_oktet_bin}.{treci_oktet_bin}.{cetvrti_oktekt_bin}')

prvi_oktet_hex =  hex(int(IPAddr_oktet[0]))
drugi_oktet_hex =hex(int(IPAddr_oktet[1]))
treci_oktet_hex =hex(int(IPAddr_oktet[2]))
cetvrti_oktet_hex =hex(int(IPAddr_oktet[3]))

print(f'IP adresa hexidecimalno je: {prvi_oktet_hex}.{drugi_oktet_hex}.{treci_oktet_hex}.{cetvrti_oktet_hex}')
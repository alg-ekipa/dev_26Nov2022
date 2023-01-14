'''
Boju pod ff2d00 treba pretvoriti u RGB

hex ff2d00
R ff
G 2d
B 00

R 255
G 45
B 0

'''
print("Unesi R, G i B kodove boje:")
R=(input("R = "))
G=(input("G = "))
B=(input("B = "))


R_hex =  int(R, 16)
G_hex =  int(G, 16)
B_hex =  int(B, 16)

print(f"HEX: {R_hex} {G_hex} {B_hex}")
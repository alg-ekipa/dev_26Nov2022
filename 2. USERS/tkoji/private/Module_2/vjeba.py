print("Input an IP address for conversion.")
octet_1 = int(input("Input the 1st octet: "))
octet_2 = int(input("Input the 2nd octet: "))
octet_3 = int(input("Input the 3rd octet: "))
octet_4 = int(input("Input the 4th octet: "))

# Binary
octet_1_bin = bin(octet_1).replace('0b','')
octet_2_bin = bin(octet_2).replace('0b','')
octet_3_bin = bin(octet_3).replace('0b','')
octet_4_bin = bin(octet_4).replace('0b','')

# Octal
octet_1_oct = oct(octet_1).replace('0o','')
octet_2_oct = oct(octet_2).replace('0o','')
octet_3_oct = oct(octet_3).replace('0o','')
octet_4_oct = oct(octet_4).replace('0o','')

print("Choosen IP address is: " + octet_1,octet_2,octet_3,octet_1, sep='.')
print("Choosen IP address in binary" + octet_1_bin, octet_2_bin, octet_3_bin, octet_4_bin, sep=".")
print("Choosen IP address in octal " + octet_1_oct, octet_2_oct, octet_3_oct, octet_4_oct, sep=".")

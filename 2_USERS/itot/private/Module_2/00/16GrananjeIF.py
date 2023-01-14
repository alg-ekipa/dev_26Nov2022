'''
Korisnik ce upsati neki broj, pitati cemo se da li je ili nije upsan broj 5

'''

a=int(input("Unesi broj:"))

if a == 5:  # if blok je uvucen za jedan TAB
    print("Broj je jedak 5")
    print("drugi ispis u IF bloku")

else: 
    print("broj nije jedank 5")
    a=int(input("Unesi broj:"))

print("Kraj")
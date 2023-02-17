'''
Korisnik ce upsati neki broj, jel broj > od 5, < od b ili =  5

'''

a=int(input("Unesi broj:"))

if a == 5:  # if blok je uvucen za jedan TAB
    print("Broj je jedak 5")
    print("drugi ispis u IF bloku")

elif a > 5:
    print("broj veci jedank 5")
else: 
    print("broj manji od 5")

print("Kraj")
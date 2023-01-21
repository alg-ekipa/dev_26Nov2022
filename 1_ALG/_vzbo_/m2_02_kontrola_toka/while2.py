    # Unesi broj u rasponu
'''
while True:
    br = int(input("unesite broj u rasponu od 10 do 20: "))
    if br >= 10 and br <= 20:
            print("Cestitamo_unijeli ste broj u rasponu ", br)
            break
    #elif type(br) == str:
    #    break
    else:
        print("Broj nije u rasponu od 10 do 20")
        print("Pokusajte ponovno")

'''
# S provjerom je li uneseni broj broj

while True:
    unos = input("unesite broj u rasponu od 10 do 20: ")
    
    while unos.isdigit() == False:
        print('Krivi unos! Morate unijeti BROJ!')
        unos = input("unesite broj u rasponu od 10 do 20: ")   
        
    if int(unos) >= 10 and int(unos) <= 20:
        print("Cestitamo_unijeli ste broj u rasponu ")
        break
    
        
    else:
        print("Broj nije u rasponu od 10 do 20")
        print("Pokusajte ponovno")
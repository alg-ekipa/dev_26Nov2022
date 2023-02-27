administrator = {
    "admin": ["Luka Lukic", "98765"]
}

def logiranje():
    uneseni_user = input('Upiši korisničko ime: ')
    while uneseni_user in administrator.keys():
        uneseni_password = input('Upiši lozinku: ')
        if uneseni_password == administrator[uneseni_user][1]:
            print(f'Dobro došao, {administrator[uneseni_user][0]} ')
        else:
            print("Unjeli ste pogrešan password. Pokušajte ponovo.")
            uneseni_password = input('Upiši lozinku: ')
            if uneseni_password == administrator[uneseni_user][1]:
                print(f'Dobro došao, {administrator[uneseni_user][0]} ')
    else:
        print("Unjeli ste pogrešno korisničko ime.")
logiranje()

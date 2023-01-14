'''
Zatražite od korisnika unos dva broja.
• Nakon unosa brojeva, ispišite:
zbroj, razliku, umnožak, količnik (rezultat djeljnja), potenciranje te modulo
unesenih brojeva
• Svaka operacija treba biti ispisana u novom redu, a ispis treba imati uključene
brojeve, znak računske operacije te rezultat.
• PRIMJER ISPISA:
• 5 + 8 = 13
• 5 - 8 = -3
• NAPOMENA Za sada kod unosa neka kod prvog unosa drugi broj NE bude 0
(nula), jer nije dopušteno dijeliti s nulom. To svakako pokušajte napraviti, ali
NE u prvom pokušaju.
'''


broj1 = int(input('Unesi prvi broj: '))
broj2 = int(input('Unesi drugi broj: '))


print(f"Zbroj unesnnih brojeva je {broj1+broj2}")
print(f"Razlika unesnnih brojeva je {broj1-broj2}")
print(f"Umnožak unesnnih brojeva je {broj1*broj2}")
if broj1 and broj2 != 0:
    print(f"Količnik unesnnih brojeva je {broj1-broj2}")
    print(f"Ostatak djeljenja broja {broj1} sa {broj2} je {broj1%broj2}")
else:
    print(f"Dijeljenje nije moguće jer jedan od brojeva je 0")
print(f"{broj1} na {broj2} potenciju je {broj1**broj2}")


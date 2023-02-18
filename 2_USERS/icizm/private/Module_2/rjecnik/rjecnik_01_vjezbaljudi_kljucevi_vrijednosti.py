ljudi = {
1 : 'Mario',
2 : 'Ivana', 
3 : 'Nikola' 
}

# Dohvat pojedinačnih vrijednosti preko ključeva
prvi = ljudi[1]
drugi = ljudi[2]
treci = ljudi[3]

print(prvi)
print(drugi)
print(treci)

print()

# Ključ kao string
stanovnistvo = {
    '12345678901' : 'Petar Perić', 
    '98765432109' : 'Marko Marić', 
    '55455455455' : 'Ana Anić', 
    '98798798798' : 'Martina M'
}

print(stanovnistvo['55455455455'])
print()

# Ispis rječnika
print(stanovnistvo)
print()

# Ispis liste parova iz rječnika ključ - vrijednost (n-terce)
print(stanovnistvo.items()) 
print()

# Ispis samo ključeva u obliku liste
print(stanovnistvo.keys())
print()
lista_kljuceva = stanovnistvo.keys()
print(lista_kljuceva)

# Ispis samo vrijednosti u obliku liste
print(stanovnistvo.values())

'''
n_torka =(4, 7, 2, 0, 1)
lista =[4, 7, 2, 0, 1]

# n-terac ili tuple - razlika od liste
print(n_torka[2])
print(lista[2])
lista[2] = 8
print (lista)
# n_torka[2]=8 ne možemo mijenjati članove jer nije lista 
'''
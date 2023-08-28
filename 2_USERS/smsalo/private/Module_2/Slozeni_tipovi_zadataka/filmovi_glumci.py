filmovi_glumci=[
    ['Superman', ['Christopher Reeves', 'Margot Kidder']],
    ['Titanic',['Leonardo DiCaprio', 'Kate Winslet']],
    ['Kum', ['Al Pacino', 'Marlon Brando']]
]

samo_glumci=[]
for film_glumac in filmovi_glumci:
    for glumci in film_glumac[1]:
        samo_glumci.append(glumci)
        
print(samo_glumci)
#sortiranje članova liste

brojevi = [3, 6, 87, 98, 23, 56, 223, 1, 8]
'''
brojevi_obrnuto = brojevi.reverse(brojevi) #obrnuti će red članova
print(f'Brojevi u našoj listi su: {brojevi}')
print(f'Obrnuta lista brojeva u našoj listi su: {brojevi_obrnuto}')
'''

brojevi_sortirano = sorted(brojevi)
print(f'Brojevi u našoj listi su: {brojevi}')
print(f'Sortirani brojevi u našoj listi su: {brojevi_sortirano}')

'''
print(brojevi)
for element in reversed(brojevi):
    print(element, end = ' ')
'''

brojevi_sortirano.reverse()
print(f'Obrnuti brojevi sa sortirane liste su: {brojevi_sortirano}')
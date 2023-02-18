'''
Napišite program koji kreira akorde na osnovu početnog tona, odnosno note.
• POJAŠNJENJE
• Akord se sastoji od tri tona koji se mogu ponavljati.
• Durski akord čine: početni ton, 4. ton te 7. ton.
Označava se samo velikim slovom početnog tona
ili velikim slovom početnog tona uz dodatak dur
• Molski akord čine: poćetni ton, 3. ton te 7. ton.
Označava se samo malim slovom početnog tona ili
malim slovom početnog tona uz dodatak mol
• Glazbena abeceda počinje od C:
C, C#, D, D#, E, F, F#, G, G#, A, A#, H
• Engleska oznaka za H ton je B tako da oni imaju A
B C D E F G tonove
• Postoji pojašnjenje u teoriji glazbe zašto je prvi ton
C, ali to sada nije važno.
'''


note = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'H']
note_prosireno = note.copy()
note_prosireno.extend(note)

'''print(note)
print ()
print(note_prosireno)'''

prvi_ton = 'x'

while prvi_ton.upper() not in note:
    prvi_ton = input("Unesite prvi ton akorda: ")
    if prvi_ton.upper() not in note:
        print ('Niste unijeli simbol koji označava ton')

else:
    index_prvog_tona = note.index(prvi_ton.upper())
    drugi_ton_mol = note_prosireno[(index_prvog_tona+2)]
    drugi_ton_dur = note_prosireno[(index_prvog_tona+3)]
    treci_ton = note_prosireno[(index_prvog_tona+6)]
    print(f"{prvi_ton.lower()} mol akord je \n{prvi_ton.upper()}, {drugi_ton_mol}, {treci_ton}")
    print(f"{prvi_ton.upper()} dur akord je \n{prvi_ton.upper()}, {drugi_ton_dur}, {treci_ton}")
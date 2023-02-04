'''Napravite aplikaciju za konverziju (u oba smjera):
• km u milju – (1 km = 0.6214 milje)
• °C u °F – (0°C = 32°F) obrnuto 𝑇(°ி) = 𝑇(°஼) ∗ (9/5) + 32
• kg u funtu (pounds) – 1 kg = 2.2046 pounds
• Litra u US galon – 1l = 0.2642 US gal
• kW (kilowatt) u ks (horsepoweer ili konjska snaga) – 1 kW = 1.3596'''

def duljina(): 
    print('Odaberi smijer konverzije: \n a. km u milje \n b. milje u km')
    odabir = input()


    if odabir == 'a': 
        km = float(input('Unesite udaljenost u kilometrima: '))
        milja = km * 0.62
        #return milja #nemamo lijepi ispis ako koristimo return
        print(f'{km} km = {milja} milja')

    if odabir == 'b': 
        m = float(input('Unesite udaljenost u miljama: '))
        kilom = m / 0.62
        #return kilom
        print(f'{m} milja = {kilom} km')

#from modul_duljina import duljina

def temperatura(): 
    print('Odaberi smijer konverzije: \n a. C u F \n b. F u C')
    odabir = input()

    if odabir == 'a': 
        C2F = float(input('Unesite temperaturu u celzijusima: '))
        far = C2F * 1.8 + 32
        
        print(f'{C2F} °C = {far} °F')

    if odabir == 'b': 
        F2C = float(input('Unesite temperaturu u farenhajtima: '))
        cel = (F2C - 32) * 0.5556
        
        print(f'{F2C} °F = {cel} °C')

def masa(): 
    print('Odaberi smijer konverzije: \n a. kilograme u funte \n b. funte u kilograme')
    odabir = input()

    if odabir == 'a': 
        K2F = float(input('Unesite težinu u kilogramima: '))
        fun = K2F * 2.2046
        
        print(f'{K2F}kg = {fun}pnd')

    if odabir == 'b': 
        F2K = float(input('Unesite težinu u funtama: '))
        kg = (F2K / 2.2046)
        print(f'{F2K}pnd = {kg}kg')

print('''Odaberite tip konverzije: 
        1. duljina
        2. temperatura
        3. masa
        4. volumen''')  

odabir = int(input())
if odabir == 1:
    duljina()
if odabir == 2: 
    temperatura()
if odabir == 3:
    masa()



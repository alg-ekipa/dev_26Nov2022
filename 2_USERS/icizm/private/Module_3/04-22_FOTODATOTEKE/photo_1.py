from PIL import Image 

foto_putanja ='python-logo.png' 
#potrebno je staviti u Terminalu putanju da radimo samo u mapi u kojoj nam se nalaze slike kako bi mogao dohvatiti putanju slike koju ćemo staviti u varijablu

foto_varijabla = Image.open(foto_putanja) # objekt tipa Image 


print(foto_varijabla)

# naredbe za izvlačenje informacija o slici 

print(foto_varijabla.format)
print(foto_varijabla.mode)
print(foto_varijabla.size)

foto_varijabla.show() # otvoriti će sliku u nekom programu za gledanje slika
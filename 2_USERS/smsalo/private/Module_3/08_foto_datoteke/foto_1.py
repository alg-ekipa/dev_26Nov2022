from PIL import Image

foto_putanja = 'python-logo.png'

foto_varijabla = Image.open(foto_putanja)

print(foto_varijabla)

print(foto_varijabla.format)
print(foto_varijabla.mode)
print(foto_varijabla.size)

foto_varijabla.show()


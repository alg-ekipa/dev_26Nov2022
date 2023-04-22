from PIL import Image

foto_putanja='C:/Users/danij/Downloads/dev_26Nov2022/1_ALG/_vzbo_/m3_05_fotodatoteke/python-logo.png'

foto_varijabla=Image.open(foto_putanja)


print(foto_varijabla)

print(foto_varijabla.format)
print(foto_varijabla.mode)
print(foto_varijabla.size)

foto_varijabla.show()




from PIL import Image

foto_putanja = 'C:/PYTHON PROGRAMIRANJE/dev_26Nov2022/2_USERS/ikuke/FOTODATOTEKE/Algebra_greyp.jpg'

foto_varijabla = Image.open(foto_putanja)

print(foto_varijabla)

print(foto_varijabla.format)
print(foto_varijabla.mode)
print(foto_varijabla.size)


foto_varijabla.show()
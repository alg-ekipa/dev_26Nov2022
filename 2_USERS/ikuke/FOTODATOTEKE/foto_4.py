from PIL import Image

foto_putanja = 'C:/PYTHON PROGRAMIRANJE/dev_26Nov2022/2_USERS/ikuke/FOTODATOTEKE/Algebra_campus.jpg'

foto_varijabla = Image.open(foto_putanja)

print(foto_varijabla)

print(foto_varijabla.format)
print(foto_varijabla.mode)
print(foto_varijabla.size)

#sadašnja veličina : (lijeva = 0, gornja=0, desna = 3992, donja = 2242)
lijeva=0 + 500; gornja = 0 + 500; desna=foto_varijabla.size[0] - 500; donja = foto_varijabla.size[1] - 500 
foto_varijabla_crop=foto_varijabla.crop((lijeva, gornja,desna,donja))
foto_varijabla_crop.show()

foto_varijabla_crop.save('C:/PYTHON PROGRAMIRANJE/dev_26Nov2022/2_USERS/ikuke/FOTODATOTEKE/Algebra_campus_crop.jpg')
foto_varijabla_crop.convert()
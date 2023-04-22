from PIL import Image

foto_putanja='Algebra_campus.jpg'

foto_varijabla = Image.open(foto_putanja)

print(foto_varijabla.size)

#sadašnja veličina: lijeva = 0, gornja=0, desna=3992, donja=2242

lijevo=0+500
gore =0+500
desno = foto_varijabla.size[0] - 500
dolje = foto_varijabla.size[1] -500

foto_varijabla_crop = foto_varijabla.crop((lijevo, gore, desno, dolje))
foto_varijabla.show()
foto_varijabla_crop.show()

print(foto_varijabla_crop.size)

foto_varijabla_crop.save('Algebra_campus_crop.jpg', 'JPEG')     #spremanje nove slike

#help(foto_varijabla.convert)
foto_varijabla_convert = foto_varijabla.convert(mode='L')
foto_varijabla_convert.show()
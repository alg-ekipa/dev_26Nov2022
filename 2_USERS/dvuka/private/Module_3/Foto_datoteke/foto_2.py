from PIL import Image

foto_putanja='C:/Users/danij/Downloads/dev_26Nov2022/1_ALG/_vzbo_/m3_05_fotodatoteke/Algebra_campus.jpg'

foto_varijabla=Image.open(foto_putanja)

print(foto_varijabla.size)

#sadašnja veličina:lijeva=0, gornja=0, desna=3992, donja=2992

lijevo=0+500
gore=0+500
desno=foto_varijabla.size[0]-500
dolje=foto_varijabla.size[1]-500

foto_varijabla_crop=foto_varijabla.crop((lijevo, gore,desno,dolje))

foto_varijabla.show()
foto_varijabla_crop.show()

foto_varijabla_crop.save('C:/Users/danij/Downloads/dev_26Nov2022/2_USERS/dvuka/private/Module_3/Foto_datoteke/Algebra_campus_crop.jpg','JPEG')


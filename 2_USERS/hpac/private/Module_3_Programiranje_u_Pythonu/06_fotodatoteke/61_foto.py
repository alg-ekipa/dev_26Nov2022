from PIL import Image

foto_putanja = 'C:/Users/hyperv/Desktop/ph/dev_26Nov2022/2_USERS/hpac/private/Module_3_Programiranje_u_Pythonu/06_fotodatoteke/Algebra_campus.jpg'

foto_varijabla = Image.open(foto_putanja)

print(foto_varijabla.size)

#sadašnja veličina: lijevo = 0, gornja = 0, desno = 3992, donja 2242

lijevo = 0+500
gore = 0+500
desno = foto_varijabla.size[0]-500
dole = foto_varijabla.size[1]-500


foto_varijabla_crop = foto_varijabla.crop((lijevo,gore,desno,dole))

#foto_varijabla.show()
#foto_varijabla_crop.show()

foto_varijabla_crop.save('C:/Users/hyperv/Desktop/ph/dev_26Nov2022/2_USERS/hpac/private/Module_3_Programiranje_u_Pythonu/06_fotodatoteke/Algebra_campus_crop.jpg','JPEG')

foto_varijabla_convert = foto_varijabla.convert(mode='L')
foto_varijabla_convert.save('C:/Users/hyperv/Desktop/ph/dev_26Nov2022/2_USERS/hpac/private/Module_3_Programiranje_u_Pythonu/06_fotodatoteke/Algebra_campus_convert.jpg','JPEG')

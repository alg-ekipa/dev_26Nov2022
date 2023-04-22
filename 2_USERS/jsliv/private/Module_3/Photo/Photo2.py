from PIL import Image

foto_putanja = "C:/Users/JulijanaS/Desktop/VisualStudioCode/dev_26Nov2022-1/2_USERS/jsliv/private/Module_3/Photo/Algebra_campus.jpg"

foto_varijabla = Image.open(foto_putanja)

print(foto_varijabla.size)

#sadašnja veličina: lijeva = 0, gornja = 0, desna = 3992, donja = 2242

lijevo = 0 + 500
gore = 0 + 500
desno = foto_varijabla.size[0] - 500
dolje = foto_varijabla.size[1] - 500

foto_varijabla_crop = foto_varijabla.crop((lijevo, gore, desno, dolje))

foto_varijabla.show()
foto_varijabla_crop.show()

foto_varijabla_crop.save("C:/Users/JulijanaS/Desktop/VisualStudioCode/dev_26Nov2022-1/2_USERS/jsliv/private/Module_3/Photo/Photo2.py/Algebra_campus_crop.jpg", "JPEG")
#ovaj save je trebao sejvati u folder Photo ali iz nekog razloga ne radi

#help(foto_varijabla.convert)
foto_varijabla.convert()
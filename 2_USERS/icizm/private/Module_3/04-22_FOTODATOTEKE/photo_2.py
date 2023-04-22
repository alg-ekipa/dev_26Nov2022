from PIL import Image

foto_putanja = 'Algebra_campus.jpg'

foto_varijabla = Image.open(foto_putanja)

print(foto_varijabla.size)
# sadašnja veličina: lijeva/left = 0, gornja/upper = 0, desna/right = 3992, donja/lower = 2242

lijevo = 0+500

gore = 0 + 500

desno = foto_varijabla.size[0] - 500

dolje = foto_varijabla.size[1] - 500


foto_varijabla_crop = foto_varijabla.crop((lijevo, gore, desno, dolje)) #cropanje slike programiranjem umjesto nekim alatom
print(foto_varijabla_crop.size)
# dvostruka zagrada kod .crop jer je cjela zagrada njegov prvi argument


foto_varijabla.show() #.show pokazuje sliku
foto_varijabla_crop.show()

foto_varijabla_crop.save('Algebra_campus_crop.jpg', 'JPEG') #.save sačuva novokropovanu sliku, drugi argument je tip slike 


#help(foto_varijabla.convert()) # .convert kad se otvori zagrada traži mode 

foto_varijabla_convert = foto_varijabla.convert(mode = 'L')

foto_varijabla_convert.show()
from PIL import Image

foto_puitanja = 'C:/Git/dev_26Nov2022/2_USERS/itot/private/Module_3/13fotodatoteke/python-logo.png'

foto_varijabla = Image.open(foto_puitanja)

print(foto_varijabla)

print(foto_varijabla.format) #format varijable
print(foto_varijabla.mode) 
print(foto_varijabla.size) #velicina objekta/slike

foto_varijabla.show() #prikaz slike



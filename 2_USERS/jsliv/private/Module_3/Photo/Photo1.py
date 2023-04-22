from PIL import Image

foto_putanja = "C:/Users/JulijanaS/Desktop/VisualStudioCode/dev_26Nov2022-1/2_USERS/jsliv/private/Module_3/Photo/python-logo.png"

foto_varijabla = Image.open(foto_putanja)

print(foto_varijabla)

print(foto_varijabla.format)
print(foto_varijabla.mode)
print(foto_varijabla.size)

foto_varijabla.show()
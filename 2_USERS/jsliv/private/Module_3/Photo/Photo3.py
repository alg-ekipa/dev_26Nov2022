from PIL import Image

foto_destination = Image.open("C:/Users/JulijanaS/Desktop/VisualStudioCode/dev_26Nov2022-1/2_USERS/jsliv/private/Module_3/Photo/Algebra_campus.jpg")
foto_source = Image.open("C:/Users/JulijanaS/Desktop/VisualStudioCode/dev_26Nov2022-1/2_USERS/jsliv/private/Module_3/Photo/python-logo.png")

foto_destination.paste(foto_source, (50,100))
foto_destination.show()
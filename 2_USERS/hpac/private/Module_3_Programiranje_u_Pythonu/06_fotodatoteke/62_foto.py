from PIL import Image

foto_destination = Image.open('C:/Users/hyperv/Desktop/ph/dev_26Nov2022/2_USERS/hpac/private/Module_3_Programiranje_u_Pythonu/06_fotodatoteke/python-logo.png')
foto_source = Image.open('C:/Users/hyperv/Desktop/ph/dev_26Nov2022/2_USERS/hpac/private/Module_3_Programiranje_u_Pythonu/06_fotodatoteke/Algebra_campus.jpg')

foto_destination.paste(foto_source, (500,300))

foto_destination.show()
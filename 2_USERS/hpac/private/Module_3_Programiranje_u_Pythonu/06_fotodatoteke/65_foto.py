from PIL import Image, ImageDraw

img = Image.open('C:/Users/hyperv/Desktop/ph/dev_26Nov2022/2_USERS/hpac/private/Module_3_Programiranje_u_Pythonu/06_fotodatoteke/python-logo.png')

img_draw = ImageDraw.Draw(img)      #kreiranje objekta na kojem je omogućeno crtanje

img_draw.rectangle((800,500,3400,2200), fill=None, outline='red',width=5)
img.show()

img_draw.ellipse((500,500,1200,950), fill=None, outline='blue', width=3)
img.show()
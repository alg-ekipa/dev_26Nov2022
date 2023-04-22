from PIL import Image, ImageDraw

img = Image.open("C:/Users/JulijanaS/Desktop/VisualStudioCode/dev_26Nov2022-1/2_USERS/jsliv/private/Module_3/Photo/python-logo.png")

img_draw = ImageDraw.Draw(img)  #kreiranje objekta na kojem je omogućeno crtanje

img_draw.rectangle((1200,1200,1400,1520), fill=None, outline="red", width=5)
img.show()

img_draw.ellipse((1200,1200,1400,1520), fill=None, outline="red", width=5)
img.show()
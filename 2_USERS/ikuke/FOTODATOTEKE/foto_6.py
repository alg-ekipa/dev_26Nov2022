from PIL import Image, ImageDraw, ImageFilter




img_path = 'C:/PYTHON PROGRAMIRANJE/dev_26Nov2022/2_USERS/ikuke/FOTODATOTEKE/python-logo.png'

img= Image.open(img_path)

img_draw= ImageDraw.Draw(img) #kreiranje objekta na kojem je omogućeno crtanje

img_draw.rectangle((80,50,400,520), fill=None, outline='red', width=5)
img_draw.ellipse((80,50,400,520), fill=None, outline='red', width=5)

img.show()

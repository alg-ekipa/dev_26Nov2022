from PIL import Image, ImageDraw

img=Image.open('C:/Users/danij/Downloads/dev_26Nov2022/1_ALG/_vzbo_/m3_05_fotodatoteke/python-logo.png')

img_draw=ImageDraw.Draw(img) #kreiranje objekata na kojem je omogućeno crtanje

img_draw.rectangle((1200,1200,1500,1520), fill=None, outline='red', width=5)
img.show()

img_draw.ellipse((1200, 1200, 1500, 1520), fill=None, outline='red', width=5)
img.show()
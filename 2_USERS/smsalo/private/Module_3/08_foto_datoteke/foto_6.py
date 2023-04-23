from PIL import Image, ImageDraw

img=Image.open('python-logo.png')

img_draw=ImageDraw.Draw(img)        #objekt za crtanje

img_draw.rectangle((200,500,500,300), fill=None, outline='red', width=5)  #veličina pravokutnika x,y pa zatim pomak od ruba
img.show()

img_draw.ellipse((700,500,1800,1000), fill=None, outline='red', width=5)
img.show()
from PIL import Image, ImageDraw

img = Image.open('C:/Users/Korisnik/Documents/dev_26Nov2022/dev_26Nov2022/2_USERS/tkoji/2. COURSES/PREDAVANJE_22_APR_2023/python-logo.png')

# img_draw = ImageDraw.Draw(img)
# img_draw.rectangle((1000,1100,77,100), fill=None, outline='blue', width=5)
# img.show()

img_draw = ImageDraw.Draw(img)
img_draw.rectangle((1001,1000,200,200) ,fill=None,outline='blue',width=1)
img_draw.ellipse((1001,1000,200,100) ,fill=None,outline='blue',width=1)
img.show()

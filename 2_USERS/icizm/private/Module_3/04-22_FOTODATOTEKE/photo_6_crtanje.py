from PIL import Image, ImageDraw

img = Image.open('python-logo.png')

# Da bi smo mogli po njemu crtati moramo napraviti image draw objekt

img_draw = ImageDraw.Draw(img) # kreiranje ojekta na kojem je omogućeno srtanje

img_draw.rectangle((500, 500, 1500, 1500), fill=None, outline='black', width=10)

img_draw.ellipse((500, 500, 1500, 1500), fill=None, outline='green', width=15) #zadnje dvije vrijednosti moraju biti veće od prve dvije

img.show()

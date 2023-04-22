from PIL import Image, ImageFilter

img = Image.open('C:/Users/hyperv/Desktop/ph/dev_26Nov2022/2_USERS/hpac/private/Module_3_Programiranje_u_Pythonu/06_fotodatoteke/Algebra_campus.jpg')

img1 = img.filter(ImageFilter.CONTOUR).show()
img2 = img.filter(ImageFilter.EDGE_ENHANCE).show()
img3 = img.filter(ImageFilter.EMBOSS).show()
img4 = img.filter(ImageFilter.SHARPEN).show()
img5 = img.filter(ImageFilter.SMOOTH).show()
img6 = img.filter(ImageFilter.BoxBlur(radius=3)).show()     #razina mutnosti
img7 = img.filter(ImageFilter.GaussianBlur(radius=3)).show()

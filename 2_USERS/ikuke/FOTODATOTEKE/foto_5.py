from PIL import Image, ImageFilter




img_path = 'C:/PYTHON PROGRAMIRANJE/dev_26Nov2022/2_USERS/ikuke/FOTODATOTEKE/Algebra_campus.jpg'

img= Image.open(img_path)

img1=img.filter(ImageFilter.CONTOUR).show()

img2=img.filter(ImageFilter.EDGE_ENHANCE).show()


img3=img.filter(ImageFilter.EMBOSS).show()

img4=img.filter(ImageFilter.SHARPEN).show()

img5=img.filter(ImageFilter.SMOOTH).show()


img6=img.filter(ImageFilter.BoxBlur(radius=100)).show()


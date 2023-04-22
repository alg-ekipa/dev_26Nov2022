from PIL import Image, ImageFilter

img = Image.open("C:/Users/JulijanaS/Desktop/VisualStudioCode/dev_26Nov2022-1/2_USERS/jsliv/private/Module_3/Photo/Algebra_campus.jpg")

img1 = img.filter(ImageFilter.CONTOUR).show()
img2 = img.filter(ImageFilter.EDGE_ENHANCE).show()
img3 = img.filter(ImageFilter.BLUR).show()
img4 = img.filter(ImageFilter.EMBOSS).show()
img5 = img.filter(ImageFilter.BoxBlur(radius=10)).show()
img6 = img.filter(ImageFilter.UnsharpMask(radius=7, percent=250, threshold=3)).show()
img7 = img.filter(ImageFilter.MedianFilter(size=7)).show()
img8 = img.filter(ImageFilter.MinFilter(size=7)).show()
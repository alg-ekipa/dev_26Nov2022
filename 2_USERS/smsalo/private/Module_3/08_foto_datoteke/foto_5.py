from PIL import Image, ImageFilter

img=Image.open('Algebra_campus.jpg')

img1 = img.filter(ImageFilter.CONTOUR).show()
img2 = img.filter(ImageFilter.EDGE_ENHANCE).show()
img3 = img.filter(ImageFilter.SHARPEN).show()
img4 = img.filter(ImageFilter.SMOOTH).show()
img5 = img.filter(ImageFilter.EMBOSS).show()
img6 = img.filter(ImageFilter.BoxBlur(radius=10)).show()
img7 = img.filter(ImageFilter.GaussianBlur(radius=5)).show()
img8 = img.filter(ImageFilter.UnsharpMask(radius=7, percent=150, threshold=7)).show()

img9 = img.filter(ImageFilter.MaxFilter(size=7)).show()

img10 = img.filter(ImageFilter.MedianFilter(size=7)).show()
img11 = img.filter(ImageFilter.MinFilter(size=7)).show()
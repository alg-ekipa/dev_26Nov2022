from PIL import Image, ImageFilter

img=Image.open('C:/Users/danij/Downloads/dev_26Nov2022/1_ALG/_vzbo_/m3_05_fotodatoteke/Algebra_campus.jpg')

img1=img.filter(ImageFilter.CONTOUR).show()
img2=img.filter(ImageFilter.EDGE_ENHANCE).show()
img3=img.filter(ImageFilter.EMBOSS).show()
img4=img.filter(ImageFilter.SHARPEN).show()
img5=img.filter(ImageFilter.SMOOTH).show()

img6=img.filter(ImageFilter.BoxBlur(radius=10)).show()
img7=img.filter(ImageFilter.GaussianBlur(radius=8)).show()

img8=img.filter(ImageFilter.UnsharpMask(radius=7, percent=250, threshold=3)).show()
img9=Image.filter(ImageFilter.MaxFilter(size=7)).show()
img10=Image.filter(ImageFilter.MedianFilter(size=7)).show()
img11=Image.filter(ImageFilter.MinFilter(size=7)).show()

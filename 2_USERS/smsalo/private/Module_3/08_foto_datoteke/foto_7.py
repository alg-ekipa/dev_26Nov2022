from PIL import Image, ImageEnhance

'''
1. Brightness
2. Contrast
3. Sharpness
4. Colour'''

img = Image.open('Algebra_campus.jpg')

img_enhance1 = ImageEnhance.Brightness(img)
img_enhance1.enhance(3).show()

img_enhance2 = ImageEnhance.Contrast(img)
img_enhance2.enhance(0.5).show()

img_enhance3 = ImageEnhance.Sharpness(img)
img_enhance3.enhance(7).show()

img_enhance4 = ImageEnhance.Color(img)
img_enhance4.enhance(0.5).show()

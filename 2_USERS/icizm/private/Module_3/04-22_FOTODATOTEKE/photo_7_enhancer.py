from PIL import Image, ImageEnhance

''' 
1. Brightness
2. Contrast
3. Sharpness
4. Color
'''

img = Image.open('Algebra_campus.jpg')

image_enhancer1 = ImageEnhance.Brightness(img)
image_enhancer1.enhance(1.5).show()

image_enhancer2 = ImageEnhance.Contrast(img)
image_enhancer2.enhance(3).show()

image_enhancer3 = ImageEnhance.Sharpness(img)
image_enhancer3.enhance(3.5).show()

image_enhancer4 = ImageEnhance.Color(img)
image_enhancer4.enhance(3.65).show()
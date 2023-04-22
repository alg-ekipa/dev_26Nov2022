from PIL import Image, ImageEnhance

"""
1. Brightnes
2. Contrast
3. Sharpness
4. Color
"""

img = Image.open("C:/Users/JulijanaS/Desktop/VisualStudioCode/dev_26Nov2022-1/2_USERS/jsliv/private/Module_3/Photo/Algebra_campus.jpg")

img_enhancer1 = ImageEnhance.Brightness(img)
img_enhancer1.enhance(3).show

img_enhancer2 = ImageEnhance.Contrast(img)
img_enhancer2.enhance(4).show()

img_enhancer3 = ImageEnhance.Sharpness(img)
img_enhancer3.enhance(7).show()

img_enhancer4 = ImageEnhance.Color(img)
img_enhancer4.enhance(4).show()

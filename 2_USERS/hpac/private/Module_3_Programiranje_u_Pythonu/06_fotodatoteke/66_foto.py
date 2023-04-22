from PIL import Image, ImageEnhance

'''
1. Brightness
2. Contrast
3. Sharpness
4. Color
'''

img = Image.open('C:/Users/hyperv/Desktop/ph/dev_26Nov2022/2_USERS/hpac/private/Module_3_Programiranje_u_Pythonu/06_fotodatoteke/Algebra_campus.jpg')

img_enhancer1 = ImageEnhance.Brightness(img)
img_enhancer1.enhance(4).show()

img_enhancer2 = ImageEnhance.Contrast(img)
img_enhancer2.enhance(4).show()

img_enhancer3 = ImageEnhance.Sharpness(img)
img_enhancer3.enhance(4).show()

img_enhancer4 = ImageEnhance.Color(img)
img_enhancer4.enhance(4).show()
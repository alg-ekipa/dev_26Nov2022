from PIL import Image, ImageDraw, ImageFilter, ImageEnhance




img_path = 'C:/PYTHON PROGRAMIRANJE/dev_26Nov2022/2_USERS/ikuke/FOTODATOTEKE/Algebra_campus.jpg'



"""
1. Brightness
2. Contrast
3. Sharpness
4. Color

"""

img= Image.open(img_path)

img_enhancer1= ImageEnhance.Brightness(img) #kreiranje objekta na kojem je omogućeno enhencanje
img_enhancer2= ImageEnhance.Contrast(img) #kreiranje objekta na kojem je omogućeno enhencanje
img_enhancer3= ImageEnhance.Sharpness(img) #kreiranje objekta na kojem je omogućeno enhencanje
img_enhancer4= ImageEnhance.Color(img) #kreiranje objekta na kojem je omogućeno enhencanje


img.show()
img_enhancer1.enhance(2).show()
img_enhancer2.enhance(2).show()
img_enhancer3.enhance(2).show()
img_enhancer4.enhance(2).show()

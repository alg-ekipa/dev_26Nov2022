from PIL import Image

photo_source = Image.open('C:/Users/Korisnik/Documents/dev_26Nov2022/dev_26Nov2022/2_USERS/tkoji/2. COURSES/PREDAVANJE_22_APR_2023/python-logo.png')
photo_dest = Image.open('C:/Users/Korisnik/Documents/dev_26Nov2022/dev_26Nov2022/2_USERS/tkoji/2. COURSES/PREDAVANJE_22_APR_2023/Algebra_campus.jpg')

# Picture in picture
photo_dest.paste(photo_source,(10,1110))

photo_trans = photo_dest.transpose(Image.FLIP_TOP_BOTTOM).show()
ph
from PIL import Image

photo_path = 'C:/Users/Korisnik/Documents/dev_26Nov2022/dev_26Nov2022/2_USERS/tkoji/2. COURSES/PREDAVANJE_22_APR_2023/python-logo.png'

photo_var = Image.open(photo_path)

print(photo_var)
print(photo_var.size)

# current size: left = 0, uppper = 0, right = 2400, lower = 2400

left = 0+500
upper = 0+500
right = photo_var.size[0] - 500
lower = photo_var.size[1] - 500

photo_var_corp = photo_var.crop((left, upper, right, lower))

print(photo_var_corp.size)

photo_var_corp.save('python_crop.png', 'PNG')

#help(photo_var.convert)
photo_var_gray = photo_var.convert(mode='L')
photo_var_gray.show()
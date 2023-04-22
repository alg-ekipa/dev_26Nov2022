from PIL import Image

foto_source = Image.open('python-logo.png')
foto_destination = Image.open('Algebra_campus.jpg')

#foto_source = Image.open('Algebra_campus.jpg')
#foto_destination = Image.open('python-logo.png')

foto_destination.paste(foto_source,(50,100))
foto_destination.show()
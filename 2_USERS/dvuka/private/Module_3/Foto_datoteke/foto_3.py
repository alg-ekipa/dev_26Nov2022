from PIL import Image

foto_source=Image.open('C:/Users/danij/Downloads/dev_26Nov2022/1_ALG/_vzbo_/m3_05_fotodatoteke/Algebra_campus.jpg')
foto_destination=Image.open('C:/Users/danij/Downloads/dev_26Nov2022/1_ALG/_vzbo_/m3_05_fotodatoteke/python-logo.png')

#slika u slici
foto_destination.paste(foto_source, (50,100))
foto_destination.show()

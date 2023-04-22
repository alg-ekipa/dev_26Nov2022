from PIL import Image


foto_putanja = 'Algebra_campus.jpg'
fotka = Image.open(foto_putanja)

foto_trans_LR=fotka.transpose(Image.FLIP_LEFT_RIGHT).show()
foto_trans_TB=fotka.transpose(Image.FLIP_TOP_BOTTOM).show()
foto_trans_R90=fotka.transpose(Image.ROTATE_90).show()

fotka.close()   #oslobodi datoteku nakon korištenja

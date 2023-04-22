from PIL import Image

foto_putanja='C:/Users/danij/Downloads/dev_26Nov2022/1_ALG/_vzbo_/m3_05_fotodatoteke/Algebra_campus.jpg'
fotka=Image.open(foto_putanja)

fotografija_trans_TB=fotka.transpose(Image.FLIP_TOP_BOTTOM).show()
fotografija_trans_LR=fotka.transpose(Image.FLIP_LEFT_RIGHT).show()
fotografija_trans_R90=fotka.transpose(Image.ROTATE_90).show()

fotografija_trans=fotka.transpose(Image.TRANSPOSE).show()
fotografija_trans=fotka.transverse(Image.TRANSVERSE).show()

fotka.close() # oslobodi datoteku nakon korištenja
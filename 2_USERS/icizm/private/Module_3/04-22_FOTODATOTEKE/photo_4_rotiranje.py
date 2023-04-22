from PIL import Image 

foto_putanja = 'Algebra_campus.jpg'
fotka = Image.open(foto_putanja)

#fotografija_trans_TB = fotka.transpose(Image.FLIP_TOP_BOTTOM).show()

#fotografija_trans_LR = fotka.transpose(Image.FLIP_LEFT_RIGHT).show()

#fotografija_trans_R90 = fotka.transpose(Image.ROTATE_90).show()

fotografija_trans_TS = fotka.transpose(Image.TRANSPOSE).show() #clockwise

fotografija_trans_TV = fotka.transpose(Image.TRANSVERSE).show() #counterclockwise

#bez.save on će samo prikazati što je napravio sa slikom

fotka.close() # oslobodi datoteku nakon korištenja




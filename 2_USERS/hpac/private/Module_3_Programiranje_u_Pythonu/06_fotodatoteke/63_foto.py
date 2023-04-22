from PIL import Image

foto_putanja = 'C:/Users/hyperv/Desktop/ph/dev_26Nov2022/2_USERS/hpac/private/Module_3_Programiranje_u_Pythonu/06_fotodatoteke/Algebra_campus.jpg'
fotka = Image.open( foto_putanja)

#fotografija_trans_TB = fotka.transpose(Image.FLIP_TOP_BOTTOM).show()
#fotografija_trans_LR = fotka.transpose(Image.FLIP_LEFT_RIGHT).show()
#fotografija_trans_R90 = fotka.transpose(Image.ROTATE_90).show()

fotografija_trans_TS = fotka.transpose(Image.TRANSPOSE).show()
fotografija_trans_TV = fotka.transpose(Image.TRANSVERSE).show()

fotka.closr() #oslobodi datoteku nakon korištenja
from PIL import Image

foto_putanja = "C:/Users/JulijanaS/Desktop/VisualStudioCode/dev_26Nov2022-1/2_USERS/jsliv/private/Module_3/Photo/Algebra_campus.jpg"
fotka = Image.open(foto_putanja)

fotografija_trans_TB = fotka.transpose(Image.FLIP_TOP_BOTTOM).show()
fotografija_trans_LR = fotka.transpose(Image.FLIP_LEFT_RIGHT).show()
fotografija_trans_R90 = fotka.transpose(Image.ROTATE_90).show()
fotografija_trans = fotka.transpose(Image.TRANSPOSE).show()

#SVAKU NAREDBU MOŽEŠ/TREBAŠ ZAKOMENTIRATI DA VIDIŠ ŠTO RADI POJEDINA NAREDBA


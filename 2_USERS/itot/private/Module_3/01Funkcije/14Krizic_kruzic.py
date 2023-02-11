


mjesta_na_ploci=['0','1','2','3','4','5','6','7','8','9']
igra=1

def ispis_ploce():
    print(mjesta_na_ploci[1], mjesta_na_ploci[2], mjesta_na_ploci[3])
    print(mjesta_na_ploci[4], mjesta_na_ploci[5], mjesta_na_ploci[6])
    print(mjesta_na_ploci[7], mjesta_na_ploci[8], mjesta_na_ploci[9])

def mjesto_upisa():
    na_koje_polje = input('Unesi zeljeno polje (1-9): ') 
 
    mjesta_na_ploci.pop(int(na_koje_polje))
    mjesta_na_ploci.insert(int(na_koje_polje),'X')


while igra == 1:
    ispis_ploce()
    mjesto_upisa()










ispis_ploce()
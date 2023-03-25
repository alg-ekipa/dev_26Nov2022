class Contact:
    def __init__(self, id, first_name):
        



try:
    with open("ljgjlgldaga  link  ") as file_reader:
        #file_data= file_reader.read()
        print(type(file_reader))
        #print(file_data)
        for red in file_reader:
            dijelovi_retka = red.split(";")
            print(dijelovi_retka)
            redni_broj = dijelovi_retka[0]
            ime = dijelovi_retka[1]
            prezime = dijelovi_retka[2]
            mob = dijelovi_retka[3].rstrip()
            print(redni_broj, ime, prezime, mob)

except Exception as e:
    print(f"Pogreška {e}")



class Contact:
    def __init__(self, id, first_name, last_name, phone):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

    def print_contact (self):
        print (f'ID: {self.id}\tName:{self.first_name}\tSurname>:{self.last_name}\t:{self.phone}')

adress_book = {}

try:
    with open ('D:/python 26.11. grupa/dev_26Nov2022-1/2_USERS/zbene/private/Module_3/25.03.2023/adresar2.txt') as file_reader:
        #file_data = file_reader.read()
        #print(type(file_reader))
        #print (file_data)
        #print (type(file_data))
        for red in file_reader:
            dijelovi_retka = red.split(';')
            #print (dijelovi_retka)
            redni_broj = dijelovi_retka [0]
            ime = dijelovi_retka [1]
            prezime = dijelovi_retka [2]
            mob = dijelovi_retka [3].rstrip
            
            contacts_object = Contact (redni_broj, ime, prezime, mob)
            contacts_object.print_contact()

except Exception as e:
    print (f'Pogreška: {e}')

#print (adress_book)

for key, value in adress_book.items():
    print (key, end=' ')
    value.print_contact()
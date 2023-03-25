class Contact:
    def __init__ (self, id, first_name, last_name, phone):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

    def print_contact(self):
         print(f'ID: {self.id}\tName: {self.first_name}\tSurname: {self.last_name}\tPhone: {self.phone}')

adress_book = {}

try:
    with open('D:/HP/dev_26Nov2022/2_USERS/hpac/private/Module_3_Programiranje_u_Pythonu/03_datoteke/adresar2.txt','r') as file_reader:
        #file_data = file_reader.read()
        #print(type(file_reader))
#       print(file_data)
#       print(type(file_data))
        for red in file_reader:
            dijelovi__retka = red.split(',')
            #print( dijelovi__retka)

            redni_broj = dijelovi__retka[0]
            ime = dijelovi__retka[1]
            prezime = dijelovi__retka[2]
            mob = dijelovi__retka[3].rstrip()

            contact_object = Contact(redni_broj, ime, prezime, mob)
            #print(redni_broj, ime, prezime, mob) 
            contact_object.print_contact()

            adress_book[redni_broj] = contact_object

except Exception as e:
        print('Pogreška: {e}')

#print(adress_book)

for key, value in adress_book.items():
     print(key, end=' ')
     value.print_contact()


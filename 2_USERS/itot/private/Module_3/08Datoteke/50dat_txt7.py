class Contact:
    def __init__(self, id, first_name, last_name, phone):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

    def print_contact(self):
        print(f'ID: {self.id}\tName: {self.first_name}\tSurname: {self.last_name}\tPhone: {self.phone}')

adress_book = {}


try: 
    with open('C:/Git/dev_26Nov2022/2_USERS/itot/private/Module_3/08Datoteke/47adresar.txt') as file_reader:
        #file_data = file_reader.read()
        #print(file_data)
        #print(type(file_data))
        for red in file_reader:

            djelovi_retka = red.split(';')
            #print(djelovi_retka)
            
            redni_broj = djelovi_retka[0]
            ime = djelovi_retka[1]
            prezime = djelovi_retka[2]
            mob = djelovi_retka[3].rstrip()

            contact_object = Contact(redni_broj,ime,prezime,mob)
            contact_object.print_contact()


            adress_book[redni_broj] = contact_object


            print(redni_broj, ime, prezime, mob )

except Exception as e:
    print(f'Pogreška: {e}')

#print(adress_book)

for key, value in adress_book.items():
    print(key, end=' ')
    value.print_contact()






class Contact:
    def __init__(self, id, first_name, last_name, phone):
        self.first_name=first_name
        self.id=id
        self.last_name=last_name
        self.phone=phone

    def print_contact(self):
        print(f'{self.id}, {self.first_name}, {self.last_name}, {self.phone}')

adress_book={}

try:
    with open('adresar2.txt', 'r') as file_reader:
        #file_data=file_reader.read()
        #print(type(file_reader))
        #print(file_data)
        #print(type(file_data))
        for red in file_reader:
            dijelovi_retka=red.split(';')
            #print(dijelovi_retka)
            redni_broj=dijelovi_retka[0]
            ime=dijelovi_retka[1]
            prezime=dijelovi_retka[2]
            mob=dijelovi_retka[3].rstrip()
            contact_object=Contact(redni_broj, ime, prezime, mob)
            contact_object.print_contact()

            adress_book[redni_broj]=contact_object
            


except Exception as e:
    print('Pogreška: {e}')

for key, value in adress_book.items():
    print(key, end=' ')
    value.print_contact()

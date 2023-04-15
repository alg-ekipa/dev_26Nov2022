import os
os.system('cls')



def vrati_putanju(datoteka):
    absolute_path = os.path.dirname(__file__)
    print(absolute_path)
    putanja=""

    i=len(absolute_path)
    for k in range (i):
        slovo=absolute_path[k]
        if slovo == "\\" :
            putanja=putanja+"/"
        else:
            putanja=putanja+slovo
    putanja=putanja+"/"
    print (absolute_path)
    print (putanja+datoteka)
    #input()

    return putanja+datoteka


file1=vrati_putanju("datoteka6.txt")





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
    with open(file1, "r") as file_reader:
        #file_data= file_reader.read()
        print(type(file_reader))
        #print(file_data)
        for red in file_reader:

            dijelovi_retka = red.split(";")
            #print(dijelovi_retka)
            redni_broj = dijelovi_retka[0]
            ime = dijelovi_retka[1]
            prezime = dijelovi_retka[2]
            mob = dijelovi_retka[3].rstrip()
            #print(redni_broj, ime, prezime, mob)

            contact_object = Contact(redni_broj,ime,prezime,mob)
            contact_object.print_contact()

            adress_book[redni_broj] = contact_object


except Exception as e:
    print(f"Pogreška {e}")

#print(adress_book)

for key, value in adress_book.items():
    print(key, end=' ')
    value.print_contact()


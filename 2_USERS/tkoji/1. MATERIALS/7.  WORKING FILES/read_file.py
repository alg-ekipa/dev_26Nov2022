class Contact:
    def __init__(self, id, first_name, last_name, mob):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.mob = mob
        
    def print_contact(self):
        print(f'ID: {self.id}\nName: {self.first_name}\nMob: {self.mob}\n')
    
address_book = {}

try:
    with open("book.txt", 'r') as file_reader:
        #file_data = file_reader.read()
        print(file_reader)
        
        for line in file_reader:
            row  = line.split(';')
            id = row[0]
            name = row[1]
            surname = row[2]
            mob = row[3].rstrip('\n')
            contact_object = Contact(id,name, surname, mob)
            #contact_object.print_contact()
            
            address_book[id] = contact_object
except Exception as e:
    print(f'Error happen: {e}')

for k,v in address_book.items():
    print(k, end=" ")
    v.print_contact()
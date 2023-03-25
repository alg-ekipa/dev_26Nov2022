
file_path = 'C:/Git/dev_26Nov2022/2_USERS/itot/private/Module_3/08Datoteke/51stolovi_rijecnik.txt'

stolovi_rjecnik = {
    '0186' : ['stol Jack', 700.00, True, '120x90x80', 'smeđa', 'drvo'],
    '0203' : ['stol Kathy', 880.00, True, '130x90x80', 'smeđa', 'drvo'],
    '1234' : ['stol Tomy', 1250.00, True, '150x100x90', 'bijela', 'drvo'],
    '4002' : ['stol Ohm', 940.00, True, '120x90x80', 'crna', 'metal'],
    '0923' : ['stol Heda', 940.00, False, '120x90x80', 'crna', 'metal'],
    '1773' : ['stol Lucas', 940.00, True, '120x90x80', 'crna', 'drvo']
   }



for x,y in stolovi_rjecnik.items():
    sifra = x
    redak = x+';'
    lista_specifikacije =list(stolovi_rjecnik[x])  
    for z in lista_specifikacije:
        redak = redak + lista_specifikacije[z] + ';'
    redak = redak + '\n'
    file_weiter = open(file_path, "a")
    file_weiter.write(redak)

'''

try: 
    with open(file_path) as file_reader:
        file_data = file_reader.read()
        print(file_data)



def ispis_opisa_datum_vrijeme(trazeni_datum,trazeno_vrijem):
    if trazeni_datum in planer_it.keys():                       #pretražuje postoji li zapis datuma
        lista_dana =list(planer_it[trazeni_datum])              #pretvara vrijednosti u listu
    for x, y in lista_dana:                                     #pretrazuje, postoji li zapis vvremena
        if x == trazeno_vrijem:                                 #x je vrijeme, y je opis u tuplesima
            return y







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

'''




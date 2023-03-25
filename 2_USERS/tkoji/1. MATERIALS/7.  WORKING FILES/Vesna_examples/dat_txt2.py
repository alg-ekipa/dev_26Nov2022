# Multiple input of persons
counter = 1
while True:
    name = input("Name: ")
    surname = input("Surname: ")
    phone = int(input("Mob: "))
    
    file_writer = open('book.txt', 'a')
    line = f'{counter};{name};{surname};{phone}\n' 
    file_writer.write(line) 
    counter += 1
    
    if input("New input: ") != 'yes':
        break

file_writer.close()
print(file_writer)

    
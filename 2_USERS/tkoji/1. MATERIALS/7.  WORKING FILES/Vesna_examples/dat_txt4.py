# with open 

counter = 1
while True:
    name = input("Name: ")
    surname = input("Surname: ")
    phone = int(input("Mob: "))
    
    try:
        with open("book.txt", 'a') as file_writer:
            line = f'{counter};{name};{surname};{phone}\n' 
            file_writer.write(line) 
            counter += 1
    
    except Exception as e:
        print(f'Error message: {e}')
    
    finally:
        file_writer.close()
        
    if input("New input (yes/no)?: ") != 'yes':
        break

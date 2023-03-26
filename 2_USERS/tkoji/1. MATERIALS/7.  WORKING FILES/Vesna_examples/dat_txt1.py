# Write to file

# method open defines a name of file we want to create and the mode ( read , write, append )



name = input("Enter name and surname: ").capitalize()
surname = input("Enter surname: ").capitalize()

file_writer = open('my_file.txt', 'w')
file_writer.write(f'\nName\t|\tSurname\n')
file_writer.write("______________________\n")
file_writer.write(f'{name}\t|\t{surname}\n')
file_writer.close()

# READING
file_reader = open('my_file.txt', 'r')
file_data = file_reader.read()
print(file_data)

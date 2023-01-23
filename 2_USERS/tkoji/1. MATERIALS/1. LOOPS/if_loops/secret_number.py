secret_number = int(input("Enter a number: "))
total_tries =  0

while secret_number != 0:
    if secret_number == 777:
        print("Congratz!")
        total_tries += 1
        break
    else:
        print("Try again!")
        total_tries += 1
    secret_number = int(input("Enter a number or type 0 to stop: "))

print(f'Bravo, you guessed the secret number in {total_tries} attempts.')
    
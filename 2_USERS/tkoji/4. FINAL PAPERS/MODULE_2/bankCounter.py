from random import randint

# To simplify the input, by default an OIB is a single integer long.
OIB_LENGTH = int(1)

# The dictionary 'client_database' acts as database where OIB ID is the key. 
# The field names in the dictionary is the list of the following values: ["Company Name", "Company Address", "IBAN", "Balance"]
# Initial balance is always 0.000
client_database = {
    "01123456789": ["Tomizmo","Los Angeles, Hollywood Boulevard", "HR314159265300123456789", 0.000],
    "0123456799": ["ALG ekipa AI solutions", "New York, Wall Street", "HR314159265300987654321", 0.000]
}

client_authentication = dict()

client_transactions = {
    "0123456789": [],
    "0123456799": []
}

def account_open(oib,company,address):
    if oib.strip().isdigit() and len(oib) == OIB_LENGTH:
        iban = iban_generator()
        pin = generate_pin_code()
        token = generate_token()
        inital_balance = float(0.00)
        client_database[oib] = [company] + [address] + [ iban ] + [ inital_balance ]
        client_transactions[oib] = [inital_balance]
        client_authentication[token] = [oib] + [pin]
        print("Your account has been successfully opened.")
        print("Your token:", token)
        print("Your PIN code:", pin)
        return True
    else: 
        print("\x1b[31mError: Incorrect OIB type or length.\x1b[0m")
        return False

def generate_pin_code():
    pin = randint(6666,9999)
    pin = str(pin)
    return pin

def generate_token():
    token = randint(666666,999999)
    token = str(token)
    return token

def iban_generator():
    bank_id = 314159265300
    account_id = randint(0000000000,9999999999)
    bank_id = str(bank_id)
    account_id = str(account_id)
    bank_id  += account_id
    bank_id = 'HR'+bank_id
    return str(bank_id)  

def account_status(oib):
    if oib in client_database.keys():
        print(f'''
        Company name : {client_database[oib][0]}
        Company address: {client_database[oib][1]}
        Company OIB : {oib}
        IBAN : {client_database[oib][2]}
        Saldo : {client_database[oib][3]} EUR.''')
        return True
    else:
        return False
    
def money_deposit(oib):
    if oib in client_database.keys():
        amount = float(input('How much money you wish to deposit? '))
        if not amount.isdigit():
            print("Error: Entered amount does not contain digits.")
        if amount <= 0:
            print("\x1b[31mError: The amount cannot be 0 or negative value.\x1b[0m")
            return False
        else: 
            balance = client_database[oib][3] + amount
            client_database[oib][3] = balance
            client_transactions[oib].append(amount)
            print("Current balance sheet :", balance, "EUR.")
            return True
    else:
        return False   

def money_withdraw(oib):
    if oib in client_database.keys():
        amount = float(input('How much money you wish to withdraw? '))
        balance = client_database[oib][3]
        if amount <= 0:
            print("\x1b[31mError: The amount cannot be 0 or negative value.\x1b[0m")
            return False
        if amount > client_database[oib][3]:
            print(f"\x1b[31mError: Not enough funds, current account balance is {client_database[oib][3]}.\x1b[0m")
        else:
            balance = client_database[oib][3] - amount
            client_database[oib][3] = balance
            client_transactions[oib].append(-abs(amount))
            print("Current balance sheet: ", balance, "EUR.")
    else:
        return False    

def account_transactions(oib):
    if oib in client_transactions.keys():
        transaction_list = client_transactions[oib][-4:]
        print("\nLast 3 transactions: ".join(str(element) for element in transaction_list))
    else:
        return False

main_menu = True
print('''
      \x1b[34mHello, welcome to ALG-EKIPA bank - your first AI driven net banking\x1b[0m''')

while main_menu == True:
    user_menu = True
    while user_menu == True:
        user_menu_choice  = input('''
            \x1b[34mAre you an existing client or you wish to open an account?\x1b[0m
            1) New client.
            2) Existing client.
            3) Exit.
            \n = ''')

        if user_menu_choice == '1':
            print('''Following information are required: OIB, Company name and address.''')
            oib = input("Please enter 11 digit OIB number: ")
            company_name = input("Please enter your company name: ")
            company_address = input("Please enter your company address: ")
            print()
                
            if account_open(oib,company_name,company_address) == True:
                print(f'\x1b[32mAccount has been created:\x1b[32m {client_database[oib]}')
   
            else:
                print("\x1b[31mPlease try again.\x1b[0m")
                user_menu = True
 
        if user_menu_choice == '2':
            user_menu = False
            pass
        
        if user_menu_choice == '3' or user_menu_choice == 'q':
            print("Thank you. Have a good day!")
            exit()
                      
    user_sub_menu = True
    authentication = input('Please enter your token ID: ')
    authorization = input('Please enter your PIN: ')
    
    while user_sub_menu == True:
        if authentication in client_authentication.keys() and authorization == client_authentication[authentication][1]:
            pass
        else:
            print("\x1b[31mSorry! The client is not in the database.\x1b[0m")
            break
            
        user_choice = input('''
            \x1b[34mPlease choose one of the following options:\x1b[0m
                    1) Display account balance.
                    2) Make a deposit.
                    3) Withdraw the funds.
                    4) Display transactions.
                    5) Logout.
                    \n = ''')
            
        if user_choice == '1':          
            if account_status(client_authentication[authentication][0]) == False:
                print("\n\x1b[31mPlease try again.\x1b[0m")
            main_menu = True
            
        if user_choice == '2':
            if money_deposit(client_authentication[authentication][0]) == False:
                print("\n\x1b[31mPlease try again.\x1b[0m")

        if user_choice == '3':
            if money_withdraw(client_authentication[authentication][0]) == False:
                print("\n\x1b[31mPlease try again.\x1b[0m")   
            
        if user_choice == '4':
            if account_transactions(client_authentication[authentication][0]) == False:
                print("\n\x1b[31mPlease try again.\x1b[0m")   
        
        if user_choice == '5' or user_choice == 'q' :
            print("\nThank you. Have a good day!")
            exit()
            break
                               
print(client_database)


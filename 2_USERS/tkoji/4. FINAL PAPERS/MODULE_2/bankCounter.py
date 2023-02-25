from random import randint

# To simplify the input, by default an OIB is a single integer long.
OIB_LENGTH = int(1)

# The dictionary 'client_database' acts as database where OIB ID is the key. 
# The field names in the dictionary is the list of the following values: ["Company Name", "Company Address", "IBAN", "Balance"]
# Initial balance is always 0.000
client_database = {
    "0123456789": ["Tomizmo","Los Angeles, Hollywood Boulevard", "HR314159265300123456789", 0.000],
    "0123456799": ["ALG ekipa AI solutions", "New York, Wall Street", "HR314159265300987654321", 0.000]
}

client_transactions = {
    "0123456789": [],
    "0123456799": []
}

def account_open(oib,company,address):
    if oib.strip().isdigit() and len(oib) == OIB_LENGTH: 
        iban = iban_generator()
        inital_balance = float(0.00)
        client_database[oib] = [company] + [address] + [ iban ] + [ inital_balance ]
        client_transactions[oib] = [inital_balance]
        return True
    else: 
        print("\x1b[31mError: Incorrect OIB type or length.\x1b[0m")
        return False

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
        balance = client_database[oib][3] + amount
        client_database[oib][3] = balance
        client_transactions[oib].append(amount)
        print("Current balance:", balance, "EUR.")
    else:
        return False    

def money_withdraw(oib):
    if oib in client_database.keys():
        amount = float(input('How much money you wish to withdraw? '))
        balance = client_database[oib][3] - amount
        client_database[oib][3] = balance
        client_transactions[oib].append(-abs(amount))
        print("Current balance:", balance, "EUR.")
    else:
        return False    

def account_transactions(oib):
    if oib in client_transactions.keys():
        transaction_list = client_transactions[oib]
        print("\nAccount transactions:".join(str(element) for element in transaction_list))
    else:
        return False

main_menu = True
print("\x1b[34mHello, welcome to ALG-EKIPA bank - your first AI driven net banking\x1b[0m")

while main_menu == True:
    user_menu = True
    while user_menu == True:
        user_menu_choice  = input('''
            \x1b[34mAre you existing client or you with to open an account?\x1b[0m
            1) New client.
            2) Existing client.
            3) Exit.
            \n = ''')

        if user_menu_choice == '1':
            print('''Following information are required: OIB, Company name and address.''')
            oib = input("Please enter 11 digit OIB number: ")
            company_name = input("Please enter your company name: ")
            company_address = input("Please enter your company address: ")
                
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
    while user_sub_menu == True:
        user_choice = input('''
            \x1b[34mPlease choose one of the following options:\x1b[0m
                    1) Display account balance.
                    2) Make a deposit.
                    3) Withdraw the funds.
                    4) Display transactions.
                    5) Logout.
                    6) <- Return 
                    \n = ''')
            
        if user_choice == '1':
            oib_identification = input('Please enter your OIB: ')
            
            if account_status(oib_identification) == False:
                print("\n\x1b[31mError: Subject with this OIB does not exist.\x1b[0m")
            main_menu = True
            
        if user_choice == '2':
            oib_identification = input('Please enter your OIB: ')
            if money_deposit(oib_identification) == False:
                print("\n\x1b[31mError: Subject with this OIB does not exist.\x1b[0m")

        if user_choice == '3':
            oib_identification = input('Please enter your OIB: ')
            if money_withdraw(oib_identification) == False:
                print("\n\x1b[31mError: Subject with this OIB does not exist.\x1b[0m")   
            
        if user_choice == '4':
            oib_identification = input('Please enter your OIB: ')
            if account_transactions(oib_identification) == False:
                print("\n\x1b[31mError: Subject with this OIB does not exist.\x1b[0m")   
        
        if user_choice == '5' or user_choice == 'q' :
            print("\nThank you. Have a good day!")
            exit()
            break
        
        if user_choice == '6':
            user_sub_menu = False
            user_menu = True
                           
print(client_database)


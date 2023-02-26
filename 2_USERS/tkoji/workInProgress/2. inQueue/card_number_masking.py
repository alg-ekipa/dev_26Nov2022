import re

print("Hello, welcome to the payment gateway!\nOur goal is to keep you security and privacy!")

#cc_number = str(input("Please input a card number: "))+
cc_number = "1234 5555 6666 7777"
formatted_number = cc_number.replace(" ",'')

if formatted_number.isdigit():
    pass
else:
    print("Card validation failed. Digits only.")
    
#print(formatted_number)

def cc_number_validator(number):
    print(number)
    if len(number) == 16:
        print("Validated card id: ", number)
    else:
        print("banana")
     
# def card_hashing(number):
#     if cc_number_format(number) == True:
#         print("Card ready for hashing.")
#         print(cc_number_format(number))
#     else: 
#         print("Card not ready for hashing.")
#         exit()
    
print(cc_number_validator(formatted_number))   
#print(card_hashing(cc_number))


import re

def string_reverse(x):
    return x [::-1]
 
check = ''

while True:
    text = input("Please input the word you whan to check if palindrome: ").lower()
    text = re.sub(r"\s+","", text, flags=re.UNICODE)
    text_reversed = string_reverse(text)
    text.lower()
    if text == text_reversed:
        print("The world is polindrome.\n")
        break
    else:
        print("This word is not polindrom.\n")
        check = input("Type 'y' if you want to check another word. ")
        if check == 'y':
            continue
        elif check == 'n':
            break
        else:
            print("Not valid input, please add 'y' to continue or 'n' to cancle.")             
            continue

# REMEMBER - a string is already a list! 
# word = input("Check if work is palindrome: ").lower()
# # THE NEXT LINE REMOVES WHITESPACE IF ANY
# word = word.replace(" ",'')
# print(word)
# word_reversed = word[::-1]

while True: 
    word = input("Check if work is palindrome or enter to quit:\n ").lower()
    word = word.replace(" ",'')
    word_reversed = word[::-1]
    if not word:
        break
    if word_reversed == word:
        print("The word is plaindrome!")
    else: 
        print("Ops! It is not.")
    

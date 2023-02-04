# REMEMBER - a string is already a list! 
input_word = input("Check if work is palindrome: ").lower()
# # THE NEXT LINE REMOVES WHITESPACE IF ANY
# word = word.replace(" ",'')
# print(word)
# word_reversed = word[::-1]

def palindrome(word):
    word = word.replace(" ",'')
    word_reversed = word[::-1]
    if word_reversed == word:
        print("The word is plaindrome!")
    else: 
        print("Ops! It is not.")
    
palindrome(input_word)


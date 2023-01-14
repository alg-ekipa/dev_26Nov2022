# PALINDROME BY TOM

# REMEMBER - a string is already a list! 
# TODO - this program does not handle the sentences ie. whitespaces.
word = input("Check if work is palindrome: ")
word = word.strip()
word_reversed = word[::-1]

if word_reversed == word:
    print("The word is plaindrome!")
else: 
    print("Ops! It is not.")
    

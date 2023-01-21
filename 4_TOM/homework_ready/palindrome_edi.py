while True: 
    word = input("Check if work is palindrome or enter to quit:\n ").lower()
    word = word.replace(" ",'')
    print(word)
    word = list(word)
    print(word)
    word_reversed = word.reverse()
    print(word_reversed)
    if not word:
        break
    if word_reversed == word:
        print("The word is plaindrome!")
    else: 
        print("Ops! It is not.")
    
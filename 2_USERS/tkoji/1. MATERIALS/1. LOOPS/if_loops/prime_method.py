def prime(choice):
    if choice % 3 == 0:
        if choice % 5 == 0:
            print("Number", choice, "is divisbale by both 3 and 5.")
        else:
            print("Number", choice, "is divisbale by 3.")
    elif choice % 5 == 0:
        print("Number", choice, "is divisbale by 5.")
        print("Result: ", choice % 5)
    else:
        print("Not divisibale by 3 or 5")
       
        
print(prime(number))
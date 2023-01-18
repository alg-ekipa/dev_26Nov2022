# DJELJIVOST S TRI

num_list = []

for num in range(1, 11):
    num_list.append(num)

for num in num_list:
    if num % 3 == 0:
        print("Number,", num, "IS divisible by 3.")
        if num % 6 == 0:
            print("Number,", num, "IS divisible by 6.")
            if num % 9 == 0:
                print("Number,", num, "IS divisible by 9.")
    else:
        print("Number", num, "IS NOT divisible by 3.")


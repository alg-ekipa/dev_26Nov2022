
tone = ["C", "D", "E", "F", "G", "A", "H"]

print("Printing DUR and MOL tones...")
print(f"DUR: { tone[0] },{ tone[3] },{ tone[4] }.")
print(f"MOL: { tone[1] },{ tone[2] },{ tone[6] }.\n")

number = int(input("Please add a first accord number to find a scale: "))
while number in [1,2,3,4,5,6,7]:
    if number in [1,2,3,4,5,6,7]:
        if number == 1:
            print(f"Number {number}st accord corresponds DUR tone: { tone[0]}")
            break
        if number == 2:
            print(f"Number {number}nd accord corresponds MOL tone: { tone[1] }.")
            break
        if number == 3:
            print(f"Number {number}rd accord corresponds MOL tone: { tone[2] }.")
            break
        if number == 4:
            print(f"Number {number}th accord corresponds DUR tone: { tone[3] }.")
            break
        if number == 5:
            print(f"Number {number}th accord corresponds DUR tone: { tone[4] }.")
            break
        if number == 7:
            print(f"Number {number}th accord corresponds MOL tone: { tone[6] }.")
            break
        if number in [6]:
            print(f"A tone '{number}' is not is not in MOL or DUR scale.")
            break
else:
        print("Number not in range.")
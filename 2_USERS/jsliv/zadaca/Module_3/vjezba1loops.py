"""
successful = True

for number in range(3):
    print("Message")
    if successful:
        print("Successful")
        break
else:
    print("I cant reach you.")
  

for x in range (5):
    for y in range(3):
        print(f"({x}, {y})")


print(type(5))
print(type(range(5)))

for x in "Python":
    print(x)

for x in [1, 2, 3, 4]:
    print(x)
"""
count = 0
for number in range(1, 20):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers.")

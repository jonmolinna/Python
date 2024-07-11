i = 1

while i < 5:
    print(i)
    i+= 1

# Example 1
number = 0
exit = True

while exit:
    print("-------------------------------")
    print("1. Add Number")
    print("2. Reset Number")
    print("3. Rest Number")
    print("4. Exit")
    print("--------------------------------")
    print("Number:", number)

    option = int(input("Option: "))

    if (option == 1):
        number += 1
    elif (option == 2):
        number = 0
    elif (option == 3):
        number -= 1
    elif (option == 4):
        exit = False
    else:
        exit = True

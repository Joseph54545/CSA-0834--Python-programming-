case = int(input("Enter Case (1 for String, 2 for Number): "))
value = input("Enter the value: ")

if case == 1 or case == 2:
    if value == value[::-1]:
        print("Palindrome")
    else:
        print("Not a Palindrome")
else:
    print("Invalid case")

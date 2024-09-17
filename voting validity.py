age = float(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are allowed to vote after", int(18 - age), "years")

x = int(input("Enter X: "))
n = int(input("Enter N: "))
choice = int(input("Enter choice (1 for Pow, 2 for Add, 3 for Sub, 4 for Mul, 5 for Div): "))

if choice == 1:
    result = 1
    for _ in range(n):
        result *= x
    print("Pow(X, N) =", result)
elif choice == 2:
    print("Add(X, N) =", x + n)
elif choice == 3:
    print("Sub(X, N) =", x - n)
elif choice == 4:
    print("Mul(X, N) =", x * n)
elif choice == 5:
    if n != 0:
        print("Div(X, N) =", x / n)
    else:
        print("Division by zero is not allowed")
else:
    print("Invalid choice")

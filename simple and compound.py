def classify_number(num):
    if num < 2:
        return "Neither prime nor composite"
        for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return "Compound number (Composite)"
    
    return "Simple number (Prime)"

number = 29
result = classify_number(number)
print(f"{number} is a {result}.")

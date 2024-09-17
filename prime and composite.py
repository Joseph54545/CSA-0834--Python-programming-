numbers = list(map(int, input("Enter numbers separated by space: ").split()))
prime_count = 0
composite_count = 0

for num in numbers:
    if num > 1:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_count += 1
        else:
            composite_count += 1

print("Prime numbers:", prime_count)
print("Composite numbers:", composite_count)

# User input
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Initialize counters for prime and composite numbers
prime_count = 0
composite_count = 0

# Loop through each number in the list
for num in numbers:
    if num < 2:
        continue  # Skip numbers less than 2 since they are neither prime nor composite
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    # If the number is prime, increase prime_count
    if is_prime:
        prime_count += 1
    else:
        composite_count += 1

# Output the result
print("Prime count:", prime_count)
print("Composite count:", composite_count)

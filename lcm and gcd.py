import math
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
gcd_result = numbers[0]
lcm_result = numbers[0]
for num in numbers[1:]:
    gcd_result = math.gcd(gcd_result, num)
    lcm_result = lcm_result * num // math.gcd(lcm_result, num)
print("GCD =", gcd_result).
print("LCM =", lcm_result)

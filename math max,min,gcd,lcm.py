import math

def lcm_using_gcd(a, b):
    gcd = math.gcd(a, b)
    lcm = (a * b) // gcd
    return lcm

# Example usage:
num1 = 12
num2 = 15
print("LCM of", num1, "and", num2, "is:", lcm_using_gcd(num1, num2))

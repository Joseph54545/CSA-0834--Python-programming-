array = [14, 16, 87, 36, 25, 89, 34]
M = int(input("Enter M (for Mth maximum): "))
N = int(input("Enter N (for Nth minimum): "))

sorted_array = sorted(array)

Mth_max = sorted_array[-M]
Nth_min = sorted_array[N-1]

print(f"{M}th Maximum Number =", Mth_max)
print(f"{N}th Minimum Number =", Nth_min)
print("Sum =", Mth_max + Nth_min)
print("Difference =", Mth_max - Nth_min)

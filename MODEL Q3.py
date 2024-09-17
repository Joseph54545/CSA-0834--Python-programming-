names = ["Banana", "Carrot", "Radish", "Apple", "Jack"]
order = input("Order (A/D): ")

if order.upper() == "A":
    names.sort()
elif order.upper() == "D":
    names.sort(reverse=True)

for name in names:
    print(name)

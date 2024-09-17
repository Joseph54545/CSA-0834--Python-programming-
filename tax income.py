taxable_income = float(input("Enter your taxable income: "))

if taxable_income <= 150000:
    tax = 0
    print("No tax.")

elif 150001 <= taxable_income <= 300000:
    tax = 0.10 * (taxable_income - 150000)
    print(f"Tax amount: {tax:.2f}")

elif 300001 <= taxable_income <= 500000:
    tax = 0.10 * 150000 + 0.20 * (taxable_income - 300000)
    print(f"Tax amount: {tax:.2f}")

else:
    tax = 0.10 * 150000 + 0.20 * 200000 + 0.30 * (taxable_income - 500000)
    print(f"Tax amount: {tax:.2f}")

positive_sum = 0
positive_count = 0
negative_sum = 0
negative_count = 0

while True:
    num = int(input("Enter the number: "))
    if num == -1:
        break
    if num > 0:
        positive_sum += num
        positive_count += 1
    elif num < 0:
        negative_sum += num
        negative_count += 1

if positive_count > 0:
    positive_avg = positive_sum / positive_count
else:
    positive_avg = 0

if negative_count > 0:
    negative_avg = negative_sum / negative_count
else:
    negative_avg = 0

print("The average of negative numbers is:", negative_avg)
print("The average of positive numbers is:", positive_avg)

date_input = input("Enter Date (DD/MM/YYYY): ")

day, month, year = map(int, date_input.split('/'))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"Given Anniversary Year: Leap Year.")
    next_anniversary_year = year + 1
    print(f"Anniversary Date: {day:02}/{month:02}/{next_anniversary_year}")
else:
    print(f"Given Anniversary Year: Non Leap Year.")
    previous_anniversary_year = year - 1
    print(f"Anniversary Date: {day:02}/{month:02}/{previous_anniversary_year}")

#!/usr/bin/python3
n = 21
# Your code should be below this line
n = int(input("Enter a number between 1 and 31: "))
if n < 1 or n > 31:
    print("Not valid")
elif (n + 13 * 14 // 5 + 2021 % 100 + 2021 % 100 // 4 + 2021 // 100 // 4 - 2 * 20) % 7 == 0 or (n + 13 * 14 // 5 + 2021 % 100 + 2021 % 100 // 4 + 2021 // 100 // 4 - 2 * 20) % 7 == 1:
    print("Weekend")
else:
    print("Weekday")



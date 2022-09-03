#!/usr/bin/python3
number = 100
# Your code should be below this line
import math
number = float(input("Enter a number: "))
if number >= 0:
    if float.is_integer(math.sqrt(5 * (number ** 2) + 4)) == 1 or float.is_integer(math.sqrt(5 * (number ** 2) - 4)) == 1:
        print("Yes")
else:
    print("No")


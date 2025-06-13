#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit_str = str(number)[-1]
last_digit = int(last_digit_str) if number >= 0 else -int(last_digit_str)
print(f"Last digit of {number} is {last_digit}", end='')
if abs(last_digit) > 5:
    print(" and is greater than 5")
elif last_digit == 0:
    print(" and is 0")
else:
    print(" and is less than 6 and not 0")

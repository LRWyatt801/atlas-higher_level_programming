#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
str1 = f"Last digit of {number} is {last} "
if last <= 5 & last != 0:
    str2 = "and is less than 6 and not 0"
elif last > 5:
    str2 = "and is greater than 5"
else:
    str2 = "and is 0"
print(f"{str1}{str2}")

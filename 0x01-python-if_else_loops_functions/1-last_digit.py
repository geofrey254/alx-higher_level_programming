#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
txt = "Last digit of {} is {}"

if last > 5:
    print(txt.format(number, last) + " and is greater than 5")
elif last == 0:
    print(txt.format(number, last) + " and is 0")
elif (last < 6) & (last != 0):
    print(txt.format(number, last-10) + " and is less than 6 and not 0")

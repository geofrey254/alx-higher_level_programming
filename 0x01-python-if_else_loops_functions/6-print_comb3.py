#!/usr/bin/python3

for i in range(0, 90):
    if i == 89:
        print("{}".format(i))
    elif (i % 11 != 0) & (i % 10 != 0) & (i % 10 != 1):
        print("{:02}".format(i), end=", ")

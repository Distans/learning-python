#!/data/data/com.termux/files/usr/bin/python3

# this program will return the sum of all numbers in an integer

import sys

try:
    n = int(input("please enter an integer: "))
except ValueError:
    print("not an integer entered")
    sys.exit(1)

total = 0

while n > 0:
    digit = n % 10
    total += digit
    n //= 10

print(total)


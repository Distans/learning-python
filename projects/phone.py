#!/data/data/com.termux/files/usr/bin/python3

import re

number = input("enter a phone number: ")
pattern = "00"
replacement = "+"

if re.match(pattern, number):
    new_number = re.sub(pattern, replacement, number)
    print(new_number)
else:
    print(number)


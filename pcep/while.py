#!/data/data/com.termux/files/usr/bin/python3

num = 1

# this would cause an infinite loop and not print anything

while num <= 6:
    if num % 3 == 0:
       print(num)


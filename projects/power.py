#!/data/data/com.termux/files/usr/bin/python3

def power(x, y):
    if y == 0:
        return 1
    else:
        return x * power(x, y-1)

print(power(2, 3))


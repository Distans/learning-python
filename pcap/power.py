#!/data/data/com.termux/files/usr/bin/python3

def power(x, y):
    if y == 0:
        return 1
    else:
        return x * power(x, y - 1)

print(power(2, 3)) # 8
# 2 * power(2, 2)
print(power(2, 2)) # 4
# 2 * power(2, 1)
print(power(2, 1)) # 2
# 2 * power(2, 0)
print(power(2, 0)) # 1


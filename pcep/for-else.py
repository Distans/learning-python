#!/data/data/com.termux/files/usr/bin/python3

for i in range(3):
    print("3")
    break
else:
    print("0")

print("if break keyword is not called inside a for loop, then else block is executed")

for i in range(0):
    print("3")
    break
else:
    print("0")


#!/data/data/com.termux/files/usr/bin/python3

for i in range(10):
    if i > 5:
        print(i)
    else:
        print("x")
else:
    print("y")

print("#####")

for i in range(10):
    if i > 5:
        print(i)
        break
    else:
        print("x")
else:
    print("y")

print("#####")

for i in range(10):
    try:
        if 10 / i == 2.0:
            break
    except ZeroDivisionError:
        print(1)
    else:
        print(2)


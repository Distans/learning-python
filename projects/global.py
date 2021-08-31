#!/data/data/com.termux/files/usr/bin/python3

y = 4

def set_y(val):
    global y
    print(y)
    y = val

set_y(1)
print(y)

z = 4

def set_z(val):
    z = val
    print(z)

set_z(1)
print(z)


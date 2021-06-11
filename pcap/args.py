#!/data/data/com.termux/files/usr/bin/python3

def sum(*args):
    y = 0
    for x in args:
        y += x
    return y

print(sum(1, 2, 3, 4, 5))

def extract(*args):
    arglist = []
    for arg in args:
        arglist.append(arg)
    return arglist

print(extract(1, 2, 3, 4, 5))


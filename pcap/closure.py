#!/data/data/com.termux/files/usr/bin/python3

def outer(par):
    loc = par
    print(par)
    print(loc)
    return 3

var = 1
outer(var)

print('#####')
print(outer(var))
# these variables do not exist outside the outer function:
# print(par)
# print(loc)
print('#####')

def outer(par):
    loc = par
    def inner():
        return loc
    return inner

var = 1
outer(var)
print(outer(var))
fun = outer(var)
print(fun())


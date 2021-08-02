#!/data/data/com.termux/files/usr/bin/python3

def fun(n):
    s = '+'
    for i in range(n):
        s += s
        yield s

for x in fun(2):
    print(x, end='')

print()
print('#####')

def fun():
    s = 'abcdef'
    for c in s[::2]:
        yield c

for x in fun():
    print(x)

print('#####')

def o(p):
    def q():
        return '+' * p
    return q

r = o(1)
s = o(2)
print(r() + s())

print('#####')

class A:
    A = 1
    def __init__(self):
        self.a = 0

print(hasattr(A, 'a'))

print('#####')

class A:
    def __init__(self, v=2):
        self.v = v
    def set(self, v=1):
        self.v += v
        return self.v

a = A()
b = a
b.set()
print(a.v)


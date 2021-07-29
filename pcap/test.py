#!/data/data/com.termux/files/usr/bin/python3

class A:
    X = 0
    def __init__(self, v=0):
        self.Y = v
        A.X += v

a = A()
b = A(1)
c = A(2)

print(a.X)
print(b.X)
print(c.X)

print('#####')

class A:
    def __init__(self, v=1):
        self.v = v
    def set(self, v):
        self.v = v
        return v

a = A()
print(a.set(a.v+1))


#!/data/data/com.termux/files/usr/bin/python3

class Example:
    c = 1
    def __init__(self, value):
        if value % 2 != 0:
            self.a = 1
        else:
            self.b = 1

example1 = Example(1)
example2 = Example(2)

try:
    print(example1.a)
except:
    print('no such attribute')

try:
    print(example1.b)
except:
    print('no such attribute')

try:
    print(example2.a)
except:
    print('no such attribute')

try:
    print(example2.b)
except:
    print('no such attribute')

print('#####')

if hasattr(example1, 'a'):
    print(example1.a)

if hasattr(example1, 'b'):
    print(example1.b)

if hasattr(example2, 'a'):
    print(example2.a)

if hasattr(example2, 'b'):
    print(example2.b)

print('#####')

print(hasattr(Example, 'a'))
print(hasattr(Example, 'b'))
print(hasattr(Example, 'c'))

print('#####')

print(hasattr(example1, 'a'))
print(hasattr(example1, 'b'))
print(hasattr(example2, 'a'))
print(hasattr(example2, 'b'))


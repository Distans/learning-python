#!/data/data/com.termux/files/usr/bin/python3

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(result.x)
print(result.y)

print('#####')

class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __truediv__(self, other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])

spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam / hello)

print('#####')

def truediv(line1, line2):
    line = "=" * len(line2)
    return "\n".join([line1, line, line2])

eggs = "eggs"
cheese = "this is not a cheese shop"

print(truediv(eggs, cheese))
print('#####')
print(truediv(cheese, eggs))


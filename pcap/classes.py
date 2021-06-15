#!/data/data/com.termux/files/usr/bin/python3

class One:
    def value1(self):
        return 1
    def value2(self):
        return 2

class Two(One):
    def value1(self):
        return 3
    def value2(self):
        return super().value2()

print(One().value1())
print(One().value2())
print(Two().value1())
print(Two().value2())


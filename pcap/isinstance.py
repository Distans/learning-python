#!/data/data/com.termux/files/usr/bin/python3

class Class1:
    pass

class Class2(Class1):
    pass

class Class3:
    pass

my_class = Class2()

print(isinstance(my_class, Class1))
print(isinstance(my_class, Class2))
print(isinstance(my_class, Class3))


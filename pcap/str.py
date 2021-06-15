#!/data/data/com.termux/files/usr/bin/python3

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"The person's name is {self.name}, their age is {self.age}"

person1 = Person('Bob', 26)
person2 = Person('Sam', 47)
print(person1, person2, sep="; ")


#!/data/data/com.termux/files/usr/bin/python3

class Person:
    def __init__(self, name, age, phone=None):
        self.name = name
        self.age = age
        self.phone = phone

    @classmethod
    def print_name(cls, name):
        print(name)

    def save(self, destination):
        destination.write(str(self))

person1 = Person('Tim', 26)

Person.print_name('Tim')
Person.print_name('Max')


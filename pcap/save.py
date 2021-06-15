#!/data/data/com.termux/files/usr/bin/python3

class Person:
    def __init__(self, first_name, last_name, age, middle_name=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.middle_name = middle_name
    def __str__(self):
        return f"First name: {self.first_name}, last name: {self.last_name}, middle name: {self.middle_name}, age: {self.age}\n"

    def save(self, destination):
        destination.write(str(self))

person1 = Person('John', 'Doe', 36, 'O.')

with open('person.txt', 'a') as file:
    person1.save(file)


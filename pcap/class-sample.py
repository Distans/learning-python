#!/data/data/com.termux/files/usr/bin/python3

class Sample:
    gamma = 0 # class variable
    def __init__(self):
        self.alpha = 1 # instance variable
        self.__delta = 3 # private instance variable

obj = Sample() # object
obj.beta = 2 # instance variable

print(obj.__dict__)

print('#####')

class HelloWorld:
    
    word1 = "hello"

    def method(self):
        print(self.word1, self.word2)

    def world(self):
        print('world')

    def hello(self):
        print('hello')
        self.world()
    def __hi(self):
        print('hi')
        self.world()

hw_obj = HelloWorld()
hw_obj.word2 = "world"
hw_obj.method()
hw_obj.hello()

try:
    hw_obj.__hi()
except:
    print('access denied')

hw_obj._HelloWorld__hi()

print('#####')

class WorkingClass:
    def __init__(self, value):
        self.profession = value

person = WorkingClass("docker")
print(person.profession)
print(type(person).__name__)
print(person.__str__())


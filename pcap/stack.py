#!/data/data/com.termux/files/usr/bin/python3

class Stack:
    # defining the class variable
    description = "A simple stack"

    def __init__(self):
        self.__stack_list = []
        
    def add(self, value):
        self.__stack_list.append(value)

    def remove(self):
        value = self.__stack_list[-1]
        del self.__stack_list[-1]
        return value

stack_object = Stack()

stack_object.add(3)
stack_object.add(2)
stack_object.add(1)

stack_object.remove()

new_stack_object = Stack()

stack_object.add(4)

new_stack_object.add(stack_object.remove())

class AddStack(Stack):
    # defining the class variable
    description = "An advanced stack"

    def __init__(self):
        Stack.__init__(self)
        # defining the instance variable
        self.capacity = 100
        # defining the private instance variable
        self.__sum = 0

    def add(self, value):
        self.__sum += value
        Stack.add(self, value)

    def remove(self):
        value = Stack.remove(self)
        self.__sum -= value
        return value

    def get_sum(self):
        return self.__sum

big_stack_object = AddStack()
# adding properties
big_stack_object.condition = "good"
big_stack_object.broken = "no"
# hacking
big_stack_object._AddStack__sum = 100

for i in range(5):
    big_stack_object.add(i)

for i in range(2):
    big_stack_object.remove()

print(stack_object.__dict__)
print(new_stack_object.__dict__)
print(big_stack_object.__dict__)

print(stack_object.description)
print(new_stack_object.description)
print(big_stack_object.description)

def show_bases(cls):
    for x in cls.__bases__:
        return x.__name__

print(show_bases(AddStack))
print(show_bases(Stack))

class MultiStack(AddStack):
    pass

print('#####')

for cls1 in [Stack, AddStack, MultiStack]:
    for cls2 in [Stack, AddStack, MultiStack]:
        print(issubclass(cls1, cls2), end='\t')
    print()

print('#####')

for obj1 in [stack_object, new_stack_object, big_stack_object]:
    for cls1 in [Stack, AddStack, MultiStack]:
        print(isinstance(obj1, cls1), end='\t')
    print()


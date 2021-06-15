#!/data/data/com.termux/files/usr/bin/python3

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)
        
    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update

class MappingSubclass(Mapping):
    def update(self, keys, values):
        print(keys)

    def print_something(self):
        print("something")

    __update = print_something

MappingSubclass([1, 2, 3])


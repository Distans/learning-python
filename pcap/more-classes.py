#!/data/data/com.termux/files/usr/bin/python3

class Class1:
    var = 100
    def fun(self):
        return 100

class Class2(Class1):
    var = 200
    def fun(self):
        return 200

class Class3(Class2):
    pass

obj1 = Class3()

print(obj1.var, obj1.fun())

class Class4:
    var = 400
    def fun(self):
        return 400

class Class5(Class1, Class4):
    pass

obj2 = Class5()

print(obj2.var, obj2.fun())


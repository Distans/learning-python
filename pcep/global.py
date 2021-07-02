#!/data/data/com.termux/files/usr/bin/python3

# outer scope affects inner scope
def func1():
    return var1
var1 = 0
func1()
print(var1)
print("#####")

# outer and inner scope variables represent different values

def func2():
    var2 = 10
    return var2
var2 = 20
print(var2)
func2()
print(var2)
print("#####")

# global keyword

def func3():
    global var3
    var3 = 30
    return var3
var3 = 40
print(var3)
func3()
print(var3)
print("#####")

# global keyword

def func4():
    global var4
    return var4
var4 = 50
func4()
print(var4)


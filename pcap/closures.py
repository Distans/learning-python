#!/data/data/com.termux/files/usr/bin/python3

def greeter(prefix):
    second_name = prefix + "Mr"
    def greet(name):
        print(f"{prefix} {name} {second_name}")
    return greet

hello = greeter("Hello,")
goodbye = greeter("Goodbye,")

hello("Kevin")
goodbye("Kyle")


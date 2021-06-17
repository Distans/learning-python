#!/data/data/com.termux/files/usr/bin/python3

def greeter(prefix):
    def greet(name):
        print(f"{prefix} {name}")
    return greet

hello = greeter("Hello,")
goodbye = greeter("Goodbye,")

hello("Kevin")
goodbye("Kyle")


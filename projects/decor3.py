#!/data/data/com.termux/files/usr/bin/python3

def decor(func):
    def wrap():
        print("8=======э(*)")
        func()
        print("(*)€=======8")
    return wrap

@decor
def print_text():
    print("Hello world!")

print_text()

#decorated = decor(print_text)
#decorated()

text = input("enter some text: ")

def uppercase_decorator(func):
    def wrapper(text):
        return text.upper()
        #your code goes here

    return wrapper

@uppercase_decorator
def display_text(text):
    return(text)

print(display_text(text))


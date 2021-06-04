#!/data/data/com.termux/files/usr/bin/python3

def hello(name, salutation):
    print(salutation, name, sep=", ")

hello(salutation="Howdy", name="Oscar")
hello("Howdy", "Oscar")

# because there is already a keyword argument we need to continue using keyword arguments
# the following line would give the error
#hello(salutation="Howdy", "Oscar")


#!/data/data/com.termux/files/usr/bin/python3

def add_five(num1, num2=5):
    return num1 + 5

# num2 is never returned
print(add_five(1,2))


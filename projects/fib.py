#!/data/data/com.termux/files/usr/bin/python3

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-2)+fib(n-1)

num = int(input("enter position: "))

print(fib(num))


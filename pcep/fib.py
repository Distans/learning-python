#!/data/data/com.termux/files/usr/bin/python3

def fib(n):
    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, a + b
        yield a

fib_gen = fib(17)
print(list(fib_gen))


#!/data/data/com.termux/files/usr/bin/python3

# factorial
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(1))
print(factorial(9))

# custom

def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)

print(fun(35)) # 3
print(fun(25)) # 56
print(fun(28)) # 31
print(fun(20)) # 101
print(fun(23)) # 81
print(fun(26)) # 58


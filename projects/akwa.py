#!/data/data/com.termux/files/usr/bin/python3

def my_func(x, y=7, *args, **kwargs):
    print(x, y, args, kwargs)

my_func(2, 3, 4, 5, 6, a=7, b=8)


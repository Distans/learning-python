#!/data/data/com.termux/files/usr/bin/python3

def func(data):
    list = [datum if datum > 90 and datum % 2 == 0 else -100 for datum in data]
    print(list)

data = [1, 2, 3, 94, 95, 96]

func(data)


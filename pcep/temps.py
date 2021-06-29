#!/data/data/com.termux/files/usr/bin/python3

from random import randint

temps = [[randint(0, 60) for h in range(24)] for d in range(31)]
print(temps)

#!/data/data/com.termux/files/usr/bin/python3

import random

a = random.randint(0, 100)
b = random.randrange(10, 100, 3)
c = random.choice( (0, 100, 3) )

print(a, b, c)


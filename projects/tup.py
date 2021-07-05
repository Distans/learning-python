#!/data/data/com.termux/files/usr/bin/python3

import random

tup = tuple(random.randint(0, 9) for _ in range(10))

print(tup)

for _ in tup:
    dup = tup.count(_)
    print(_, ":", dup)


#!/data/data/com.termux/files/usr/bin/python3

import random

my_list = list(range(1, 100))
print(random.choice(my_list))
print(random.sample(my_list, 10))


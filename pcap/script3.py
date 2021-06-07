#!/data/data/com.termux/files/usr/bin/python3

from modules.module1 import extract_upper as e_u, extract_lower as e_l

print(e_u.__doc__)
print(e_u("Hello World"))
print(e_l.__doc__)
print(e_l("Hello World"))


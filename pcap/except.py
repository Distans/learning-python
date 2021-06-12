#!/data/data/com.termux/files/usr/bin/python3

import sys

try:
    print(f"Name is {sys.argv[1]}")
except IndexError as err:
    print(f"Error: {err}")
else:
    print(f"else")
finally:
    print(f"finally")

assert len(sys.argv) >= 2, "not enough arguments"

if len(sys.argv) < 2:
    raise Exception('not enough arguments')


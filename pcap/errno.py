#!/data/data/com.termux/files/usr/bin/python3

import errno

try:
    f = open("fake.txt", "r")
except OSError as err:
    if err.errno == errno.ENOENT:
        print("No such file")



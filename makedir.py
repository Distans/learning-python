#!/data/data/com.termux/files/usr/bin/python3

import os

def makedir(arg):
    os.mkdir(arg)

dirname = input("dir name: ")

try:
    makedir(dirname)
except FileExistsError:
    print("dir exists")


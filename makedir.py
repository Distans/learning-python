import os

def makedir(arg):
    os.mkdir(arg)

dirname = input("dir name: ")

try:
    makedir(dirname)
except FileExistsError:
    print("dir exists")


import sys

x = input("please enter an even number: ")

try:
    x % 2 == 0
except:
    print("error 13: not an even number")
    sys.exit(13)


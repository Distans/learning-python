#!/data/data/com.termux/files/usr/bin/python3

thing = (number for number in range(1, 11))
type(thing)

first_run = list(thing)
print(first_run)

# generators are disposable!

second_run = list(thing)
print(second_run)


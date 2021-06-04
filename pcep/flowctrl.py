#!/data/data/com.termux/files/usr/bin/python3

# part 1
print("part 1")

letter = 'c'
if letter < 'e':
    print(1)
if letter == 'b' or letter >= 'c':
    print(2)
# this is executed as an if-else block:
if letter < 'a':
    print(3)
else:
    print(4)

# part 2
print("part 2")

letter = 'a'
if letter < 'b':
    print(1)
# this is executed as an if-else block:
if letter == 'b' or letter > 'c':
    print(2)
elif letter <= 'a':
    print(3)
else:
    print(4)


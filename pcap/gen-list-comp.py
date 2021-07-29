#!/data/data/com.termux/files/usr/bin/python3

def pow_of_two(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2

t = [x for x in pow_of_two(9)]
print(t)

l = []

for i in range(300):
    if i in pow_of_two(9):
        l.append(i)

print(l)


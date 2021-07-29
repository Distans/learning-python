#!/data/data/com.termux/files/usr/bin/python3

the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
the_gen = (1 if x % 2 == 0 else 0 for x in range(10))

print(len(the_list))

try:
    print(len(the_gen))
except TypeError:
    print('object of type "generator" has no len()')

for v in the_list:
    print(v, end=' ')
print()

for v in the_gen:
    print(v, end=' ')
print()


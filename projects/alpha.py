#!/data/data/com.termux/files/usr/bin/python3

# this program takes 3 names, sorts them alphabetically and prints them out

name1 = input("enter name 1: ").capitalize()
name2 = input("enter name 2: ").capitalize()
name3 = input("enter name 3: ").capitalize()

if name1 < name2 < name3:
    print(name1)
    print(name2)
    print(name3)
elif name1 < name3 < name2:
    print(name1)
    print(name3)
    print(name2)
elif name2 < name1 < name3:
    print(name2)
    print(name1)
    print(name3)
elif name2 < name3 < name1:
    print(name2)
    print(name3)
    print(name1)
elif name3 < name1 < name2:
    print(name3)
    print(name1)
    print(name2)
elif name3 < name2 < name1:
    print(name3)
    print(name2)
    print(name1)

# 123 132 213 231 312 321

names = []
names.append(name1)
names.append(name2)
names.append(name3)
print(sorted(names))


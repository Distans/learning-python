#!/data/data/com.termux/files/usr/bin/python3

# this program counts a string's "weight"

my_str = input("please provide a string: ")

total_weight = 0

for item in my_str:
    item_weight = ord(item)
    total_weight += item_weight

print(total_weight)


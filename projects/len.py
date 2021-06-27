#!/data/data/com.termux/files/usr/bin/python3

my_list = [1, 2, 3, 4, 5, 6, 7]
total = 0

print(len(my_list))

for i in range(len(my_list)):
    total += my_list[i]

print(total)


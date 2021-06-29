#!/data/data/com.termux/files/usr/bin/python3

my_list = [1, 2, 3, 4, 5]
print(my_list)

new_list = my_list[1:-1]
print(new_list)

empty_list = my_list[-1:1]
print(empty_list)

reverse_list = my_list[::-1]
print(reverse_list)

my_list_link = my_list
my_list_copy = my_list[:]
my_list.insert(0, 0)
print(my_list)
print(my_list_link)
print(my_list_copy)


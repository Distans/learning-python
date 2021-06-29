#!/data/data/com.termux/files/usr/bin/python3

#task 1

my_list = [1, 2, 3]

print(my_list)

print(list(range(len(my_list))))

for v in range(len(my_list)):
    my_list.insert(1, my_list[v])
    print(my_list)

print("#####")

#task 2

new_list = [[0, 1, 2, 3] for i in range(2)]
print(new_list)
print(new_list[1][1])

print("#####")

#task 3

some_list = [[3 - i for i in range(3)] for j in range(3)]

print(some_list)

s = 0

for i in range(3):
    s += some_list[i][i]
    print(s)


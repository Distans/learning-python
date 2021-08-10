#!/data/data/com.termux/files/usr/bin/python3

people = []

for i in range(5):
    people.append(0)

for i in range(8):
    people.append(1)

for i in range(4):
    people.append(2)

for i in range(3):
    people.append(3)

people = tuple(people)
mean = sum(people) / len(people)
print(mean)

var_list = []

for i in people:
    var_item = (i - mean)**2
    var_list.append(var_item)

var_tuple = tuple(var_list)
variance = sum(var_tuple) / len(var_tuple)
print(variance)


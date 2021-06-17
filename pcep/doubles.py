#!/data/data/com.termux/files/usr/bin/python3

def double_values(list1):
    doubles = []
    for num in list1:
        doubles.append(str(num * 2))
    return doubles

list2 = [1, 2, 3, 4]
print(double_values(list2))
print(type(double_values(list2)))
# join method converts a list to a string
print("_".join(double_values(list2)))
print(type("_".join(double_values(list2))))


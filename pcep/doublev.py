#!/data/data/com.termux/files/usr/bin/python3

def double_values(list):
    doubles = []
    for num in list:
        doubles.append(str(num*2))
    return doubles

list1 = [1, 2, 3, 4]

joined = (" ".join(double_values(list1)))
print(type(joined))
print(" ".join(double_values(list1)))
print("".join(double_values(list1)))

doubled = double_values(list1)
print(type(doubled))
print(double_values(list1))


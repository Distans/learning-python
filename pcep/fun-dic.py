#!/data/data/com.termux/files/usr/bin/python3

# function

def f(x):
    if x == 0:
        return 0
    return x + f(x - 1)

print(f(3)) # 6 (3+3)
print(f(2)) # 3 (2+1)
print(f(1)) # 1 (1+0)
print(f(0)) # 0 (0)

print("#####")

# dictionary

dict = {'one':'two', 'three':'one', 'two':'three'}
print(dict)

v = dict['one']
print(v) # two

#print(range(len(dict)))

for k in range(len(dict)):
    v = dict[v]
    print(v) # three \ one \ two

print(dict[v]) # three

print(v) # two


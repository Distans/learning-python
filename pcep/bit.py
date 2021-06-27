i = int(input("integer 1: "))
j = int(input("integer 2: "))

print("binary integer 1:")
print(bin(i))

print("binary integer 2:")
print(bin(j))

print("bitwise AND:")
print(i & j)

print("bitwise OR:")
print(i | j)

print("bitwise XOR:")
print(i ^ j)

print("bitwise NOT integer 1:")
print(~ i)

print("bitwise NOT integer 2:")
print(~ j)

print("shift both integers to the left by one bit:")
print(i << 1)
print(j << 1)

print("shift both integers to the right by one bit:")
print(i >> 1)
print(j >> 1)


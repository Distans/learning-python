#!/data/data/com.termux/files/usr/bin/python3

names = ['Alice', 'Lance', 'Bob', 'Mike']
names2 = names
names.append('Brock')

# sorted function does not change the variable
sorted(names2)

print(names)
print(names2)
print(sorted(names2))


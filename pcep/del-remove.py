#!/data/data/com.termux/files/usr/bin/python3

# creating a list
names = ['John', 'Sam', 'Joe']
print(names)
print("removing Joe from 'names' with remove method")
names.remove('Joe')
print(names)

# creating a dictionary
ages = {'John': 35, 'Sam': 50, 'Joe': 22}
print(ages)
print("removing Joe from 'ages' with del keyword")
del ages['Joe']
print(ages)

print("remove is a method for lists, del is a keyword for dictionaries")


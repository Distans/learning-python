#!/data/data/com.termux/files/usr/bin/python3

ages = {'Keith': 30, 'Levi': 25, 'John': 27}
age = ages.get('Kevin')

# get method prevents KeyError and returns None
print(age)

age1 = ages['Michael']


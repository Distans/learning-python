#!/data/data/com.termux/files/usr/bin/python3

from functools import reduce

domain = [1, 45, 13, 2, 53, 675]

# map
mapped = (list(map(lambda x: x*3+1, domain)))
print(mapped)

# filter
filtered = (list(filter(lambda x: x % 2 == 0, mapped)))
print(filtered)

# reduce
reduced = reduce(lambda acc, num: acc + num, filtered, 0)
print(reduced)

# sorted (creates a new list)
words = ['Al', 'Matt', 'pike', 'Pike', 'nail', 'weed', 'riff']
print(sorted(words))
print(sorted(words, key=lambda x: x.lower()))

# sort method (changes the existing list)
words.sort()
print(words)
words.sort(key=str.lower)
print(words)



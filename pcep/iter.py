#!/data/data/com.termux/files/usr/bin/python3

# list of vowels

vowels = ['a', 'e', 'i', 'o', 'u']
vowels_iter = iter(vowels)

for _ in vowels:
    print(next(vowels_iter))



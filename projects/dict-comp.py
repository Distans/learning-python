#!/data/data/com.termux/files/usr/bin/python3

word = 'abracadabra'
count = {letter: word.count(letter) for letter in set(word)}
print(count)


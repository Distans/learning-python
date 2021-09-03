#!/data/data/com.termux/files/usr/bin/python3

text = input("enter some text: ")
dict = {}
for i in text:
    k = i
    v = text.count(i)
    dict[k] = v
print(dict)


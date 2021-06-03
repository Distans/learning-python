#!/data/data/com.termux/files/usr/bin/python3

pair1 = ('a', 'b', 'c')
pair2 = ('d', 'e', 'f')
index = 0

while index < len(pair1):
    for item in pair2:
        print(pair2[index], item)
    index += 1


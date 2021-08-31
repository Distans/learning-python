#!/data/data/com.termux/files/usr/bin/python3

count = 0

while count < 10:
    if count % 2 == 0:
        count += 1
        continue
    print(count)
    count += 1


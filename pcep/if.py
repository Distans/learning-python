#!/data/data/com.termux/files/usr/bin/python3

for num in range(1, 10, 2):
    if num % 3:
        print(num)

print(list(range(1, 10, 2)))

print(list(map(lambda x: x%3, list(range(1, 10,2)))))


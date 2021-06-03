#!/data/data/com.termux/files/usr/bin/python3

file = open('hello.txt', 'a')
file.write('hello, world!')
file.write('\nhow are you?\n')
file.close()
file = open('hello.txt')
print(file.read())

file = open('hello.txt', 'a')
file.write('hello, world!')
file.write('\nhow are you?')
file.close()
file = open('hello.txt')
print(file.read())

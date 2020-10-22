length = 10
star = "*"
for i in range(length):
    for j in range(length - i):
        print(" ", end = '')
    print(star)
    star += "**"


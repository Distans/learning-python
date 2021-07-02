#!/data/data/com.termux/files/usr/bin/python3

# break is called, so else is not called
while True:
    print("hi")
    break
else:
    print("bye")

# break is not called, so else is called
while False:
    print("hi")
    break
else:
    print("bye")


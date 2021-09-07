#!/data/data/com.termux/files/usr/bin/python3

tweet = input("Say something ")

try:
    if len(tweet) > 42:
        raise ValueError("Too long")
except:
    print("Error")
else:
    print("Posted")

if len(tweet) < 3:
    raise ValueError("Too short")


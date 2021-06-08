#!/data/data/com.termux/files/usr/bin/python3

def makeword():
    word = ""
    userword = str(input("please enter a word: "))
    for c in userword:
        word += c
        yield word

print(list(makeword()))


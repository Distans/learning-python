#!/data/data/com.termux/files/usr/bin/python3

s = input("please provide a word or a phrase for a hashtag: ")

def hash_tag_gen(text):
    hash = "#"
    text1 = hash + text
    text2 = text1.replace(" ", "")
    return text2

print(hash_tag_gen(s))


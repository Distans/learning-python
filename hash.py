s = input()

def hash_tag_gen(text):
    hash = "#"
    text1 = hash + text
    text2 = text1.replace(" ", "")
    return text2

print(hash_tag_gen(s))


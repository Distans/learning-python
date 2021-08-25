#!/data/data/com.termux/files/usr/bin/python3

text = input("provide some text ")
text = text.split()
sum_letters = [] 
sum_words = len(text)
for item in text:
    sum_letters.append(len(item))
sum_letters = sum(sum_letters)
awl = sum_letters / sum_words
print(awl)


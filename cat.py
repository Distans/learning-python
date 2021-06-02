#!/data/data/com.termux/files/usr/bin/python3

text = input("enter some text here: ")
text_len = len(text)
print('{}'.format('-' * (text_len + 2)))
print('[{}]'.format(text))
print('{}'.format('-' * (text_len + 2)))

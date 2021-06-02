#!/data/data/com.termux/files/usr/bin/python3

string = input('enter some text: ')

def palindrome(string):
    return string.casefold() == string[::-1].casefold()

if palindrome(string) is True:
    print(string, 'is a palindrome')
else:
    print(string, 'is not a palindrome')


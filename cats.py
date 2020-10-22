#! /data/data/com.termux/files/usr/bin/python3

print('how many puppies do you have?')
puppies = input()
try:
    if int(puppies) > 3:
        print('too many puppies')
    elif int(puppies) < 0:
        print('please provide positive number of puppies')
    else:
        print('that is not too many puppies')

except ValueError:
    print('please provide a number')

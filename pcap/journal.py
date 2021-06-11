#!/data/data/com.termux/files/usr/bin/python3

with open('diary.txt', 'a+') as my_file:
    my_file.write(input("how was your day? "))
    my_file.write("\n")
    my_file.seek(0)
    print(my_file.read())


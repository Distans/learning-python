#!/data/data/com.termux/files/usr/bin/python3

year = int(input("please provide year number: "))

if year % 4 != 0:
    print("common")
elif year % 100 != 0:
    print("leap")
elif year % 400 != 0:
    print("common")
else:
    print("leap")



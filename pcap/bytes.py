#!/data/data/com.termux/files/usr/bin/python3

mybytes = b'Tim'
print(mybytes)
print(mybytes[1])
print(mybytes[2])
print(type(mybytes))

mybarray = bytearray(mybytes)
mybarray[1:2] = b'ea'
print(mybarray)
mybarray[1:2] = b''
mybarray[1] = 105
mybarray[2] = 109
print(mybarray)

with open('diary.txt', 'rb') as myfile:
    barray = bytearray(4)
    myfile.readinto(barray)
    print(barray)
    newbarray = bytearray(myfile.read(7))
    print(newbarray)



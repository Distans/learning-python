#!/data/data/com.termux/files/usr/bin/python3
data = [
  [23, 11, 5, 14],
  [8, 32, 20, 5]
]
color = input("brown, blue, green or black? ")
total = sum(data[0])+sum(data[1])
brown_total = data[0][0]+data[1][0]
blue_total = data[0][1]+data[1][1]
green_total = data[0][2]+data[1][2]
black_total = data[0][3]+data[1][3]
if color == "brown":
    print(int(brown_total / total * 100))
elif color == "blue":
    print(int(blue_total / total * 100))
elif color == "green":
    print(int(green_total / total * 100))
elif color == "black":
    print(int(black_total / total * 100))


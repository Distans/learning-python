#!/data/data/com.termux/files/usr/bin/python3

class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @staticmethod
    def area(width, height):
        return width * height

w = int(input("enter width "))
h = int(input("enter height "))

print(Shape.area(w, h))


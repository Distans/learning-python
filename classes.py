#!/data/data/com.termux/files/usr/bin/python3

class Cat:
    """
    docstring
    """
    def __init__(self, color, eye_color):
        """
        docstring
        """
        self.color = color
        self.eye_color = eye_color

    def describe(self):
        print(f"{self} is a {self.color} cat with {self.eye_color} eyes")



#!/data/data/com.termux/files/usr/bin/python3

class Noise:
    def __init__(self):
        pass

    @property
    def music(self):
        return 0

merzbow = Noise()
try:
    merzbow.music = 1
except AttributeError as ae:
    print('no music allowed!', ae)


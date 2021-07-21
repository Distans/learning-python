#!/data/data/com.termux/files/usr/bin/python3

class A:
    def spam(self):
        print(1)

class B(A):
    def spam(self):
        print(2)
        super().spam()

B().spam()

b = B()

b.spam()


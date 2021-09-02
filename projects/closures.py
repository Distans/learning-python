#!/data/data/com.termux/files/usr/bin/python3

def salutation(title):
    def surname(name):
        return f"{title} {name}"
    return surname 

mr = salutation("Mr")
ms = salutation("Ms")
name = "Smith"

print(mr(name))
print(ms(name))


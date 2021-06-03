#!/data/data/com.termux/files/usr/bin/python3

def body(height, weight):
    return weight / (height/100) ** 2

h = float(input("please enter your height, cm: "))
w = float(input("please enter your weight, kg: "))

index = round(body(h, w), 1)

print(f"your body mass index is {index}")

if index >= 25.0:
    print("you are in danger")
elif index >= 18.5 and index <= 24.9:
    print("you are ok")


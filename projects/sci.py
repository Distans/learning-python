#!/data/data/com.termux/files/usr/bin/python3

number1 = str(3*10**8)
print(number1)
print(number1.count("0"))

number2 = str(int(3e8))
print(number2)
print(number2.count("0"))

print(number1 == number2)


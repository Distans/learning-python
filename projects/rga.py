#!/data/data/com.termux/files/usr/bin/python3
data = {
    "100-90": 25, "42-01": 48, "55-09": 12, "128-64": 71, "002-22": 18, "321-54": 19, "097-32": 33, "065-135": 64, "99-043": 80, "111-99": 11, "123-019": 5, "109-890": 72, "132-123": 27, "32-908": 27, "008-09": 25, "055-967": 35, "897-99": 44, "890-98": 56, "344-32": 65, "43-955": 59, "001-233": 9, "089-111": 15, "090-090": 17, "56-777": 23, "44-909": 27, "13-111": 21, "87-432": 15, "87-433": 14, "87-434": 23, "87-435": 11, "87-436": 12, "87-437": 16, "94-121": 15, "94-122": 35, "80-089": 10, "87-456": 8, "87-430": 40
}
age = int(input("enter age "))
adults = []
teens = []
for value in data.values():
    if value >= 18:
        adults.append(value)
    elif value < 18:
        teens.append(value)
revenue = len(adults)*20 + len(teens)*5
#print(revenue)
new_adults = []
new_teens = []
for value in data.values():
    if value >= age:
        new_adults.append(value)
    elif value < age:
        new_teens.append(value)
new_revenue = len(new_adults)*20 + len(new_teens)*5
#print(new_revenue)
print(int(((new_revenue-revenue)/revenue)*100))



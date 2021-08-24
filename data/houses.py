#!/data/data/com.termux/files/usr/bin/python3

import numpy as np

data = np.array([150000, 125000, 320000, 540000, 200000, 120000, 160000, 230000, 280000, 290000, 300000, 500000, 420000, 100000, 150000, 280000])
avg = np.mean(data)
std = np.std(data)
print(avg)
print(std)
lst = []
for item in data:
    diff = avg - item
    lst.append(abs(diff))
print(lst)
fnl = []
for item in lst:
    if item < std:
        fnl.append(item)
print(fnl)
print(len(fnl))
print(len(data))
prc = (len(fnl) / len(data)) * 100
print(prc)


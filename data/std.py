#!/data/data/com.termux/files/usr/bin/python3

players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]
print(sorted(players))
pl_tup = tuple(players)
mean = sum(pl_tup) / len(pl_tup)
print(mean)
var_list = []
for i in players:
    item = (i - mean) ** 2
    var_list.append(item)
var_tup = tuple(var_list)
variance = sum(var_tup) / len(var_tup)
stdev = variance ** 0.5
print(stdev)
final = []
for i in players:
    item = i - mean
    if item < 0:
        item = 0 - item
    final.append(item)
print(final)
end = []
for i in final:
    if i < stdev:
        end.append(i)
print(len(end))


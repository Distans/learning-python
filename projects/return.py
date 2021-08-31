#!/data/data/com.termux/files/usr/bin/python3

def get_item(lst, itm):
    if itm in lst:
        return lst.index(itm)
    #return

mal = [13, 66, 47, 74, 128]

print(get_item(mal, 47))
print(get_item(mal, 27))


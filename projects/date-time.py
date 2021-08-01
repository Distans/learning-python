#!/data/data/com.termux/files/usr/bin/python3

from datetime import date, datetime
import time
import datetime as dt
from datetime import time as tm

today = date.today()
print(type(today))
print(today)
print(today.year)
print(today.month)
print(today.day)
time.sleep(0.666)

timestamp = time.time()
#print(type(timestamp))
print(timestamp)
print(time.ctime(timestamp))
#print(time.gmtime(timestamp))
#print(time.localtime(timestamp))
time.sleep(0.666)

d = date.fromtimestamp(timestamp)
print(d)
time.sleep(0.666)

d = d.replace(year=1984, month=11, day=5)
print(d)
print(d.weekday())
time.sleep(0.666)

print(datetime.today())
print(datetime.now())
print(datetime.utcnow())
dt = datetime.now()
print(type(dt))
print(dt.timestamp())
print(dt.strftime('%Y*%m*%d'))
time.sleep(0.666)

t = dt.time()
print(type(t))
print(t)
print(t.strftime('%Y*%m*%d*%H*%M*%S'))
# it looks like the date part is empty in the time object hence it is set to default
time.sleep(0.666)

print(datetime.strptime("2084-11-05-16-20-13", "%Y-%m-%d-%H-%M-%S"))
t = tm(6, 6, 6)
print(type(t))
print(t.strftime("%H#%M#%S"))
time.sleep(0.666)

dt1 = datetime(2020, 11, 5)
dt2 = datetime.now()
dtd = dt2 - dt1
print(type(dtd))
print(str(dtd).split())


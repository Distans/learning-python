import datetime

last_beer = datetime.date(2020, 9, 11)

print(last_beer.weekday())
print(last_beer.isoweekday())

today = datetime.date(2020, 9, 25)

diff = today - last_beer

print(diff)


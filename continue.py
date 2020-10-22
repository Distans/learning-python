count = 0

while count < 100:
    if count % 2 == 0:
        count += 1
        continue
    print('counting odd numbers: ', count)
    count += 1


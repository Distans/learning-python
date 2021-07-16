#!/data/data/com.termux/files/usr/bin/python3

# DISCLAIMER. DO NOT RUN THIS SCRIPT AS YOU WILL NOT BE ABLE TO INTERRUPT IT.

sec = 0

while True:
    try:
        print(sec)
        sec += 1
    except KeyboardInterrupt:
        print('denied')


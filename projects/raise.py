#!/data/data/com.termux/files/usr/bin/python3

def fun(n):
    try:
        return 0 / n
    except:
        print('exception raised')
#        raise
        return 1

try:
    fun(0)
except ZeroDivisionError:
    print('exception reraised')

#raise


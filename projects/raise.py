#!/data/data/com.termux/files/usr/bin/python3

def fun(n):
    try:
        return 0 / n
    except:
        print('an exception raised:')
        raise

try:
    fun(0)
except:
    print('cannot divide by zero')

try:
    fun('0')
except:
    print('cannot divide by a string')


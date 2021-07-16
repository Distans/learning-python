x = '5,0'

try:
    int(x)
except:
    raise Exception('cannot convert str to int')


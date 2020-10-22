print('input symbol:')
symbol = input()

print('input width:')
width = int(input())

print('input height:')
height = int(input())

def box(symbol, width, height):

    if len(symbol) != 1:
        raise Exception('symbol must be of length 1')
    
    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)

box(symbol, width, height)

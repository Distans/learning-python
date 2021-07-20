#!/data/data/com.termux/files/usr/bin/python3

def menu(item1, item2, *args, **kwargs):
    print(f'required: {item1}')
    print(f'required: {item2}')
    print(f'optional: {args}')
    print(f'optional: {kwargs}')

menu('start', 'quit', 'demo', 'credits', graphics='medium', sound='high')


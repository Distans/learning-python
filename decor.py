def inspect(func, *args):
    print(f"running {func.__name__}")
    val = func(*args)
    return(val)

def combine(a, b):
    return a + b


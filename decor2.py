def inspect(func, *args):
    def wrapped(*args, **kwargs):
        print(f"running {func.__name__}")
        val = func(*args, **kwargs)
        return val
    return wrapped

@inspect
def combine(a, b):
    return a + b


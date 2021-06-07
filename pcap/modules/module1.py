#!/data/data/com.termux/files/usr/bin/python3

if __name__ == "__main__":
    print("running module as a script")

def extract_upper(phrase):
    """
    returns uppercase letters

    >>> extract_upper("Hello World")
    ['H', 'W']
    """
    return list(filter(str.isupper, phrase))

def extract_lower(phrase):
    """
    returns lowercase letters
    >>> extract_lower("Hello World")
    ['e', 'l', 'l', 'o', 'o', 'r', 'l', 'd']
    """
    return list(filter(str.islower, phrase))

if __name__ == "module":
    print("imported successfully")

print(f"name in module.py: {__name__}")

if __name__ == "__main__":
    import doctest
    doctest.testmod()


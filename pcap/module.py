#!/data/data/com.termux/files/usr/bin/python3

if __name__ == "__main__":
    print("running module as a script")

def extract_upper(phrase):
    return list(filter(str.isupper, phrase))

def extract_lower(phrase):
    return list(filter(str.islower, phrase))

if __name__ == "module":
    print("imported successfully")

print(f"name in module.py: {__name__}")


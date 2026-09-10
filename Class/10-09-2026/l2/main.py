def add(a, b):
    return a + b

def password(pwd):
    if len(pwd) == 0:
        return False
    
    upper = any(char.isupper() for char in pwd)
    lower = any(char.islower() for char in pwd)
    digit = any(char.isdigit() for char in pwd)
    return upper and lower and digit
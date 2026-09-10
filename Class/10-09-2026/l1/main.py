def add(a, b):
    return a + b


def mul(a, b):
    return a * b

def email(email):
    if email.count('@') == 0 or email.count('@') > 1:
        return False
    if email.count('.') == 0:
        return False
    if len(email[:email.find('@')]) <= 2:
        return False
    return True
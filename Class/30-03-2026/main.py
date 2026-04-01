a = 1
b = 2
def first():
    global a
    print(a)
    print(b)
    
    c = 3
    print(c)
    a += 1 
    
    
first()


def fibonacci(n):
    if (not n) or n == 1:
        return True
    n1, n2 = 0, 1
    
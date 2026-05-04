def make_accumulator(start=0):
    def accumulator(number):
        nonlocal start
        start += number
        return start
    
    return accumulator

acc = make_accumulator(10)
print(acc(5))  
print(acc(3)) 
print(acc(-2))


def make_startswith_checker(prefix):
    def checker(string):
        return string.startswith(prefix)
    
    return checker

check_py = make_startswith_checker("py")
print(check_py("python"))  
print(check_py("pyramid")) 
print(check_py("java"))    
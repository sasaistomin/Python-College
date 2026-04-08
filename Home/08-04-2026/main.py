#1
def sumNum(*args):
    return sum(args)
print(sumNum(1,2,3))



#2
def printPerson(**kwargs):
    for k, v in kwargs.items():
        print(f'{k}: {v}')
print(printPerson(name='Sasha', age=14))



#3
def printCountry(country='Ukraine'):
    print(country)
printCountry()
printCountry('USA')



#4
def printInfo(name, age):
    print(f'I`m {name}, i am {age} ears old')
printInfo('Sasha', 17)



#5
def multiplier(n):
    def factor(number):
        return number * n
    return factor
double = multiplier(2)
print(double(10))  



#6
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5)) 



#7
def sum_recursive(n):
    if n == 1:
        return 1
    return n + sum_recursive(n - 1)
print(sum_recursive(10))



#9
u = lambda x: x**2
print(u(4))



#10
data = [('apple', 10), ('banana', 2), ('orange', 5)]
sorted_data = sorted(data, key=lambda item: item[1])
print(sorted_data) 



#11
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  
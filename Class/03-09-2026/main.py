# class Car:
#     def __init__(self, name, ear):
#         self.__name = name
#         self.__ear = ear

#     def __str__(self):
#         return f'Name: {self.__name}\nEar: {self.__ear}'
#     def Comfort(self):
#         return 'Good'


# car = Car('Skoda', 2000)
# print(car)

# class Sedan(Car):
#     def __init__(self, name, ear):
#         super().__init__(name, ear)

#     def __str__(self):
#         return f'Name: {self.__name}\nEar: {self.__ear}'

#     def Cardo(self):
#         return 'Transport'

# bmw = Sedan('BMW', 2010)

# class HotRod(Sedan, Car):
#     pass

# cars = HotRod('Mazda', 2012)

# class Pet:
#     def __init__(self, name, type='pet'):
#         self.name = name
#         self.type = type
#         if self.type == 'cat':
#             self.sound = 'meau'
#         elif self.type == 'dog':
#             self.sound = 'gav'

#     def Sound(self):
#         return self.sound


# class Cat(Pet):
#     def __init__(self, name):
#         super().__init__(name, type='cat')


# m = Cat('rit')
# print(m.Sound())

# class Car:
#     def __init__(self, name, year):
#         self.name = name
#         self.year = year

#     @property
#     def name(self):
#         return self.__name

#     @name.setter
#     def name(self, name):
#         self.__name = name

#     def __str__(self):
#         return f'Name: {self.name}\nYear: {self.year}'

# audi = Car(name='Audi', year=2020)
# print(audi.year)

# audi.name = "BMW"
# print(audi)

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    def __str__(self):
        return f'Name: {self.__name}\nAge: {self.__age}'

p1 = Person('Sasha', 19)
print(p1)
p1.age = 20
print(p1)
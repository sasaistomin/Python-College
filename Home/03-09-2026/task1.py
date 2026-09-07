class Car: 
    def __init__(self, name, year, autorCar, engineD, color, price):
        self._name = name
        self._year = year
        self._autorCar = autorCar
        self._engineD = engineD
        self._color = color
        self._price = price

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def color(self):
        return self._name
    @color.setter
    def color(self, color):
        self._color = color

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, price):
        self._price = price

    def __str__(self):
        return f'Name: {self._name}\nYear: {self._year}\nAutor car: {self._autorCar}\nEngine displacement: {self._engineD}\nColor: {self._color}\nPrice: {self._price}$'

audi = Car('Audi A6', 2026, 'Audi', 3.4, 'white', 60000)
# print(audi)



class Book:
    def __init__(self, name, year, publisher, autor, genre, price):
        self._name = name
        self._year = year
        self._publisher = publisher
        self._autor = autor
        self._genre = genre
        self._price = price

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, price):
        self._price = price

    def __str__(self):
        return f'Name: {self._name}\nYear: {self._year}\nPublisher: {self._publisher}\nAutor: {self._autor}\nGenre: {self._genre}\nPrice: {self._price}'

book = Book('Dog name money', 2018, '-', '-', 'Bisnes book', 1600)
# print(book)

class Stadium:
    def __init__(self, name, dataStart, country, city, count):
        self._name = name
        self._dataStart = dataStart
        self._country = country
        self._city = city
        self._count = count

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    def __str__(self):
        return f'Name: {self._name}\nDate of start work: {self._dataStart}\nCounty: {self._country}\nCity: {self._city}\nCount: {self._count}'

s = Stadium('Liret', 1990, 'UK', 'London', 10000)
print(s)
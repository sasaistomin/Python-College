class Balanse: 
    def __init__(self, n, curr='USD'):
        self._balanse = n
        self._curr = curr

    def __add__(self, other):
        if self._curr == other._curr:
            return Balanse(self._balanse + other._balanse, self._curr)
        else: 
            return Balanse(self._balanse, self._curr)
    
    def __sub__(self, other):
        if self._curr == other._curr:
            return Balanse(self._balanse - other._balanse, self._curr)
        else: 
            return Balanse(self._balanse, self._curr)

    def __str__(self):
        return f'{self._balanse}\n{self._curr}'

if __name__ == '__main__':
    balanse = Balanse(100, 'USD')
    print(balanse)
    deposit = Balanse(200, 'UAH')
    print(deposit)
from main import Balanse
import pytest

def test_add_to_balanse():
    user = 10
    money = 5
    curr = 'UAH'
    baln = Balanse(user, curr)
    dep = Balanse(money, curr)
    baln = baln + dep
    assert baln._balanse == user + money 

def test_sub_same_currency():
    baln = Balanse(100, 'USD')
    dep = Balanse(40, 'USD')
    result = baln - dep
    assert result._balanse == 60
    assert result._curr == 'USD'

def test_sub_different_currency():
    baln = Balanse(100, 'USD')
    dep = Balanse(40, 'EUR')
    result = baln - dep
    assert result._balanse == 100
    assert result._curr == 'USD'

def test_str_representation():
    baln = Balanse(150, 'UAH')
    assert str(baln) == "150\nUAH"

@pytest.mark.parametrize('ini, ch, ex', [
    (100, 50, 150),
    (0, 20, 20),
    (50, 0, 50)
])
def test_add_par(ini, ch, ex):
    b1 = Balanse(ini, 'USD')
    b2 = Balanse(ch, 'USD')
    reset = b1 + b2
    assert reset._balanse == ex
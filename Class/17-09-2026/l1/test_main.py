import pytest
from main import add, double, triple, lists

def test_add():
    assert add(1, 4) == 5


@pytest.mark.parametrize('n, expected', [(0,0), (2, 4), (3, 6), (2, 4)])
def test_double(n, expected):
    assert double(n) == expected


triple_list = [
    (1, 2, 3, 2),
    (1, 3, 5, 3),
    (2, 3, 10, 5)
]

@pytest.mark.parametrize('a, b, c, ex', triple_list)
def test_triple(a, b, c, ex):
    assert triple(a, b, c) == ex

    

lists_data = [
    ([1, 2, 3, 3, 4, 5, 4, 5, 2], [1, 2, 3, 4, 5]),
    ([1, 1, 1], [1]),
]

@pytest.mark.parametrize('Lists, ex', lists_data)
def test_lists(Lists, ex):
    assert lists(Lists) == ex
from main import *
import pytest 

def test_add():
    assert add(5,5) == 10
    assert add(1, 3) == 4
    assert add('Hello', 'World') == 'HelloWorld'


def test_mul():
    assert mul(4, 5) == 20
    assert mul(1, -1) == -1
    assert mul(2, 2) == 4

def test_email_at_positive():
    assert email('test@gmail.com') == True

def test_email_at_negative():
    assert email('testgmail.com') == False
    assert email('test@gmailcom') == False
    assert email('te@gmail.com') == False
import pytest

def add(x,y):
    return x+y

@pytest.mark.parametrize('num1, num2, res', [ (1, 2, 3), ('Hi ', 'Everyone', 'Hi Everyone'), (9.2, 1.7, 10.899999999999999) ] )

def test_add(num1, num2, res):
    i=0
    assert add(num1, num2) == res
    print("TestCase_", i , "passed")
    i += 1


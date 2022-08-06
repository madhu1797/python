import pytest
import logging

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

@pytest.fixture
def var():
    a=1
    b=2
    return [a, b]

def test_math_var1():
    assert var[0]==1  
    LOGGER.info("TestCase_1 passed")

def test_math_var2():
    assert var[1]==2
    LOGGER.info("TestCase_2 passed")



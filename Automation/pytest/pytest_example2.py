import pytest
import logging

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_math_add():
    a=1
    b=2
    c=a+b
    assert c == 3  
    LOGGER.info("TestCase_1 passed")

def test_math_sub():
    a=1
    b=2
    c=b-1
    assert c == 1
    LOGGER.info("TestCase_1 passed")

@pytest.mark.mul
def test_mul():
    a=1
    b=2
    c=a*b
    assert c == 2
    LOGGER.info("TestCase_1 passed")



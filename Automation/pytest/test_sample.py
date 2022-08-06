import pytest
import logging

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

pytest.flag = 0

def test_eggs():
    LOGGER.info('eggs info')
    LOGGER.warning('eggs warning')
    LOGGER.error('eggs error')
    LOGGER.critical('eggs critical')
    assert True

@pytest.mark.check
def test_always_passes():
    assert True
    LOGGER.info("TestCase_1 passed")

@pytest.mark.skip(reason="testing skip functionality")
def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISES"
    LOGGER.info("TestCase_2 passed")

@pytest.mark.skipif(pytest.flag > 0, reason = "Flag not set")
def test_reversed():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]
    pytest.flag += 1
    LOGGER.info("TestCase_3 passed")
    print(pytest.flag)


@pytest.mark.skipif(pytest.flag >= 1, reason="Flag not more than 1")

def test_some_primes():
    assert 37 in {
        num
        for num in range(1, 50)
        if num != 1 and not any([num % div == 0 for div in range(2, num)])
    }
    LOGGER.info("TestCase_4 passed")

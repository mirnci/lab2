import pytest
from library import sieve_of_eratosthenes

# Тестирование решета Эратосфена
def test_sieve_valid():
    assert sieve_of_eratosthenes(10) == [2, 3, 5, 7]

def test_sieve_invalid():
    with pytest.raises(ValueError):
        sieve_of_eratosthenes(1)
    with pytest.raises(ValueError):
        sieve_of_eratosthenes(-5)
    with pytest.raises(ValueError):
        sieve_of_eratosthenes("abc")
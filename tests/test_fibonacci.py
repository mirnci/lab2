import pytest
from library import fibonacci

# Тестирование Фибоначчи
def test_fibonacci_valid():
    assert fibonacci(5) == [0, 1, 1, 2, 3]

def test_fibonacci_invalid():
    with pytest.raises(ValueError):
        fibonacci(-1)
    with pytest.raises(ValueError):
        fibonacci(0)
    with pytest.raises(ValueError):
        fibonacci("abc")

import pytest
from library import bubble_sort


# Тестирование сортировки
def test_bubble_sort_valid():
    assert bubble_sort([3, 1, 2]) == [1, 2, 3]

def test_bubble_sort_invalid():
    with pytest.raises(ValueError):
        bubble_sort("not a list")